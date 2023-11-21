from enum import Enum
from pydantic import BaseModel


class Permission(Enum):
    Users = 'Users'
    Patients = 'Patients'
    Records = 'Records'


class Role(BaseModel):
    id: int
    name: str
    permissions: list[Permission]


roles = [
    Role(id=0, name='Administrator', permissions=[
        Permission.Users,
        Permission.Patients,
        Permission.Records,
    ]),
    Role(id=1, name='Doctor', permissions=[
        Permission.Patients,
        Permission.Records,
    ]),
    Role(id=2, name='Manager', permissions=[
        Permission.Records,
    ])
]
