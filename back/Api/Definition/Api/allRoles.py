from Domain.Enums.roles import Role, roles
from ..router import router


@router.get("/allRoles")
def roles() -> list[Role]:
    return roles
