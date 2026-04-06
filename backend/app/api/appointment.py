from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.appointments import AppointmentCreate
from app.services import appointment_service

router = APIRouter(prefix="/appointments", tags=["Appointments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_appointment(data: AppointmentCreate, db: Session = Depends(get_db)):
    try:
        return appointment_service.create_appointment(db, data)
    except  Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
def list_appointments(db: Session = Depends(get_db)):
    return appointment_service.list_appointments(db)