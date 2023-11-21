from fastapi import Depends
from sqlalchemy.orm import Session
from Api.Users.Models.userDto import UserDto
from Domain.Enums.roles import Permission
from Domain.user import User
from utils import get_db, get_current_user, check_permission, create_pagination_result
from ..router import router
from ...paginationResultModel import PaginationResultModel


@router.get("/list")
def user_list(page: int,
              db: Session = Depends(get_db),
              current_user: User = Depends(get_current_user)
              ) -> PaginationResultModel[UserDto]:
    check_permission(current_user, Permission.Users)
    return create_pagination_result(db, User, UserDto, page,
                                    lambda x: UserDto(
                                        id=str(x.Id),
                                        email=x.Email,
                                        name=x.Name,
                                        roleId=x.RoleId,
                                        isActive=x.IsActive,
                                    ))
