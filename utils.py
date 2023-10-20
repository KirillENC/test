import os
import types
from fastapi import Security, HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer
from Api.paginationResultModel import PaginationResultModel
from Domain.Enums.roles import roles
from Domain.user import User
from database import SessionLocal, SQLALCHEMY_DATABASE_URL
import random
import string
import jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
import re
from yoyo import read_migrations
from yoyo import get_backend
from datetime import date
from sqlalchemy import desc

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

ALGORITHM = "HS256"

page_size = 50

sender_email = os.getenv("SENDER_EMAIL", "Skvortsov.Kirill@endocrincentr.ru")
sender_email_password = os.getenv("SENDER_EMAIL_PASSWORD", "Qw123456")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def get_user_token(user: User):
    expire = datetime.utcnow() + timedelta(minutes=480)
    return jwt.encode({"userId": str(user.Id), "email": user.Email, "exp": expire}, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(db: Session = Depends(get_db),
                     token: str = Security(OAuth2PasswordBearer(tokenUrl="/api/identity/getTokenByLoginAndPassword"))):
    try:
        jwt_decode = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except:
        raise HTTPException(status_code=401)
    user = db.query(User).filter(User.Id == jwt_decode['userId']).first()
    if not user.IsActive:
        raise HTTPException(status_code=401)
    return user


def check_permission(user: User, permission):
    if not have_permission(user, permission):
        raise HTTPException(status_code=405)


def have_permission(user: User, permission):
    role = next(filter(lambda r: r.id == user.RoleId, roles))
    find_permission = filter(lambda p: p.value == permission.value, role.permissions)
    if len(list(find_permission)) == 0:
        return False
    return True

prefixes = []


def add_route(router_base: APIRouter, method: types.ModuleType):
    if method.router.prefix not in prefixes:
        router_base.include_router(method.router)
        prefixes.append(method.router.prefix)


def get_page(db: Session, entity, page: int):
    return db.query(entity).limit(page_size).offset(page * page_size)


def create_pagination_result(db, entity, dto_type, page, mapper_lambda, filter_lambda=lambda x: x):
    result_query = filter_lambda(db.query(entity))
    print("Query: ", str(result_query))
    return PaginationResultModel[dto_type](
        page=page,
        rows=list(map(mapper_lambda, result_query.limit(page_size).offset(page * page_size))),
        totalCount=result_query.count())


def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def run_migration():
    backend = get_backend(SQLALCHEMY_DATABASE_URL)
    os.environ["PYTHONUTF8"] = "1"
    migrations = read_migrations('./migrations')
    print('migrations.len: ' + str(len(migrations)))
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def get_first_letter_with_dot(name):
    if name is None or name == '':
        return ''
    return f'{name[0]}.'


def get_patient_full_name(patient):
    if patient.Patronymic is None or patient.Patronymic == '':
        return f'{patient.Surname} {get_first_letter_with_dot(patient.Name)}'
    return f'{patient.Surname} {get_first_letter_with_dot(patient.Name)} {get_first_letter_with_dot(patient.Patronymic)}'


def create_cascade_filters(filters):
    if len(filters) == 0:
        return lambda q: q

    if len(filters) == 1:
        return filters[0]

    def apply_filters(q, index):
        if index == len(filters) - 1:
            return filters[index](q)
        else:
            return filters[index](apply_filters(q, index + 1))

    return lambda q: apply_filters(q, 0)


class FluentFilter:
    filters: list
    sort_type: str
    sortField: str

    def __init__(self, sort_type, sort_field):
        self.sort_type = sort_type
        self.sort_field = sort_field
        self.filters = []

    def build(self, id_field_default_sort=None):
        if len(self.filters) == 0:
            return lambda q: q
        if id_field_default_sort is not None:
            return lambda q: create_cascade_filters(self.filters)(q).order_by(id_field_default_sort)
        else:
            return lambda q: create_cascade_filters(self.filters)(q)

    def use_filter(self, field_value, filter):
        condition = field_value is not None and field_value != '' and field_value != False
        if condition:
            self.filters.append(filter)
        return self

    def use_join(self, join):
        self.filters.append(join)
        return self

    def sort_core(self, field_name, asc, decs):
        if field_name == self.sort_field:
            if self.sort_type == 'asc':
                self.filters.append(asc)
            if self.sort_type == 'desc':
                self.filters.append(decs)

        return self

    def use_sort(self, field_name, field):
        asc = lambda q: q.order_by(field)
        decs = lambda q: q.order_by(desc(field))
        self.sort_core(field_name, asc, decs)
        return self

    def use_sort_reverse(self, field_name, field):
        asc = lambda q: q.order_by(desc(field))
        decs = lambda q: q.order_by(field)
        self.sort_core(field_name, asc, decs)
        return self
