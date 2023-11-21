from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from Domain.base import Base
from datetime import datetime


class Record(Base):
    __tablename__ = "Records"
    Id: Mapped[str] = mapped_column(primary_key=True)
    DoctorId: Mapped[str] = mapped_column()
    PatientId: Mapped[str] = mapped_column()
    DateTimeStart: Mapped[datetime] = mapped_column()
