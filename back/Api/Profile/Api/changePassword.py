import hashlib
from fastapi import Depends
from sqlalchemy import update
from sqlalchemy.orm import Session
from Domain.user import User
from utils import get_db, get_current_user
from ..router import router
from ...operationResultModel import OperationResultModel


@router.post("/changePassword")
def change_password(old_password: str,
                    new_password: str,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)
                    ) -> OperationResultModel[str]:
    if current_user.PasswordHash == hashlib.sha512(old_password.encode('utf-8')).hexdigest():
        db.execute(update(User).where(User.Id == current_user.Id).values(
            PasswordHash=hashlib.sha512(new_password.encode('utf-8')).hexdigest()))
        db.commit()
        return OperationResultModel(data='password changed')
    else:
        return OperationResultModel(error='wrong old password')
