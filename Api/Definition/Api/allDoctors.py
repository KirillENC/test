from Domain.Enums.roles import Role, roles
from Domain.user import User
from ..Models.definitionModel import DefinitionModel
from ..router import router
from sqlalchemy.orm import Session
from fastapi import Depends
from utils import get_db


@router.get("/allDoctors")
def doctors(db: Session = Depends(get_db)) -> list[DefinitionModel]:
    doctor_role = next(filter(lambda r: r.name == 'Doctor', roles))
    doctors = db.query(User).filter(User.RoleId ==doctor_role.id).all()
    return list(map(lambda d: DefinitionModel(
        name=d.Name,
        value=str(d.Id)
    ), doctors))
