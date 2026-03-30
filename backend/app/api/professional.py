from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import Session

from app.core.database import SessionLocal
from app.schemas.professional import ProfessionalCreate
from app.services import professional_service

router = APIRouter(prefix="/professionals", tags=["Professionals"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_professional(
    professional: ProfessionalCreate,
    db: Session = Depends(get_db)):

    try:
        return professional_service.ProfessionalCreate(db, professional)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
def list_professionals(db: Session = Depends(get_db)):
    return professional_service.list_professional(db)