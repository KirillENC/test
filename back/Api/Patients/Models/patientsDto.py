from datetime import datetime
from pydantic import BaseModel
from pydantic.schema import Optional


class PatientDto(BaseModel):
    id: str
    qmsId: str
    name: Optional[str] = ''
    surname: Optional[str] = ''
    patronymic: Optional[str] = ''
    gender: int
    dob: datetime
