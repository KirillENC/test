from fastapi import Depends
from Domain.Enums.roles import Permission
from Domain.user import User
from sqlalchemy import update
from sqlalchemy.orm import Session
from utils import get_db, get_current_user, check_permission
from ..router import router


@router.post("/changeActivity")
def change_activity(id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    check_permission(current_user, Permission.Users)
    user = db.query(User).filter(User.Id == id).first()
    db.execute(update(User).where(User.Id == id).values(
        IsActive=not user.IsActive))
    db.commit()
    return 'activity changed'
