from pydantic import BaseModel


class ProfessionalCreate(BaseModel):
    name: str
    specialty: str
    license_number: str
