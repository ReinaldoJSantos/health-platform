from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from app.core.database import Base

class Appointments(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    professional_id = Column(Integer, ForeignKey("professionals.id"))

    date = Column(DateTime, nullable=False)
    status = Column(String, default="sheduled")