from pydantic import BaseModel
from datetime import datetime

class AppointmentCreate(BaseModel):
    paciente_id: int
    professional_id: int
    date: datetime