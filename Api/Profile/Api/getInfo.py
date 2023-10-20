from fastapi import Depends
from Api.Profile.Models.profileInfo import ProfileInfo
from Domain.user import User
from utils import get_current_user
from ..router import router


@router.get("/getInfo")
def get_info(current_user: User = Depends(get_current_user)) -> ProfileInfo:
    return ProfileInfo(id=str(current_user.Id), name=current_user.Name, role=current_user.RoleId)
