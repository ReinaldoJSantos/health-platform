from sqlalchemy import Column, Integer, String, Date
from app.core.database import Base


class Patient(Base):
    __table__name__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cpf = Column(String, nullable=False, unique=True)
    birth_date = Column(Date)