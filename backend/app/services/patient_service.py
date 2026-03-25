from sqlalchemy.orm import Session
from app.models.patient import Patient
from app.schemas.patient import PatientCreate

def create_patient(db: Session, patient: PatientCreate):
    # validade cpf duplicado
    existing = db.query(Patient).filter(Patient.cpf == patient.cpf).first()
    if existing:
        raise ValueError("CPF já cadastrado")
    db_patient = Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


def get_patients(db: Session):
    return db.query(Patient).all()