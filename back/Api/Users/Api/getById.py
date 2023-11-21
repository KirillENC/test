from fastapi import Depends
from sqlalchemy.orm import Session
from Api.Users.Models.userDto import UserDto
from Domain.Enums.roles import Permission
from Domain.user import User
from utils import get_db, get_current_user, check_permission
from ..router import router


@router.get("/getById")
def get_user(id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) -> UserDto:
    check_permission(current_user, Permission.Users)
    user = db.query(User).filter(User.Id == id).first()

    return UserDto(
        id=str(user.Id),
        email=user.Email,
        name=user.Name,
        roleId=user.RoleId,
        isActive=user.IsActive,
    )