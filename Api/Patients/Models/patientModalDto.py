from datetime import datetime
from pydantic import BaseModel


class PatientModalDto(BaseModel):
    id: str
    qmsId: str
    name: str
    surname: str
    patronymic: str
    gender: int
    dob: datetime
