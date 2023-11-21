from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from Domain.base import Base
from datetime import datetime


class Patient(Base):
    __tablename__ = "Patients"
    Id: Mapped[str] = mapped_column(primary_key=True)
    Name: Mapped[str] = mapped_column()
    Surname: Mapped[str] = mapped_column()
    Patronymic: Mapped[str] = mapped_column()
    Gender: Mapped[int] = mapped_column()
    Dob: Mapped[datetime] = mapped_column()
