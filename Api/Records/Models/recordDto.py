from pydantic import BaseModel


class RecordDto(BaseModel):
    id: str
    doctor: str
    patient: str
    start: str
