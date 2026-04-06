from sqlalchemy.orm import Session
from app.models.professional import Professional
from app.schemas.professional import ProfessionalCreate


def create_professional(
    db: Session, professional: ProfessionalCreate):
    existing = db.query(Professional).filter(Professional.license_number == professional.license_number).first()

    if existing:
        raise Exception("Professional already exists")

    db_prof = Professional(**professional.dict())
    db.add(db_prof)
    db.commit()
    db.refresh(db_prof)

    return db_prof


def list_professional(db: Session):
    return db.query(Professional).all()

