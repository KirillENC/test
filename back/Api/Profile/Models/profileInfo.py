from pydantic import BaseModel


class ProfileInfo(BaseModel):
    id: str
    name: str
    role: int
