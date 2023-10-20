from pydantic import BaseModel


class IdentityResult(BaseModel):
    isSuccess: bool
    access_token: str = None
