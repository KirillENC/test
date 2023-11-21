from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from Domain.base import Base


class User(Base):
    __tablename__ = "Users"
    Id: Mapped[str] = mapped_column(primary_key=True)
    Email: Mapped[str] = mapped_column(String(90))
    Name: Mapped[str] = mapped_column(String(90))
    RoleId: Mapped[int] = mapped_column()
    IsActive: Mapped[bool] = mapped_column()
    PasswordHash: Mapped[str] = mapped_column(String(200))

