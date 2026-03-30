from pydantic import BaseModel


def classProfessionalCreate(BaseModel):
    name: str
    specialty: str
    license_number: str
