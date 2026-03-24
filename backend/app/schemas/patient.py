from pydantic import BaseModel
from datetime import date


class PatientCreate(BaseModel):
    name: str
    cpf: str
    birth_date: date
