from sqlalchemy import Column, Integer, String, Date
from app.core.database import Base

class Professional(Base):
    __tablename__ = "professionals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialty = Column(String, nullable=False)
    license_number = Column(String, unique=True, nullable=False)
