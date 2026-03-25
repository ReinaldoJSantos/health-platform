from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.patient import Patient
from app.schemas.patient import PatientCreate
from app.services import patient_service

router = APIRouter(prefix="/patients", tags=["Patients"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
async def create_patient(
            patient: PatientCreate,
            db: Session = Depends(get_db)
):
   try:
       return patient_service.create_patient(db, patient)
   except Exception as e:
       raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
def list_patients(db: Session = Depends(get_db)):
    return patient_service.get_patients(db)