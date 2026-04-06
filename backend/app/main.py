from fastapi import FastAPI
from app.core.database import engine, Base

from app.models import patient, professional, appointment
from app.api import patient
from app.api import professional
from app.api import appointment




app = FastAPI(title="Healt Plataform API")
app.include_router(patient.router)
app.include_router(professional.router)
app.include_router(appointment.router)


Base.metadata.create_all(bind=engine)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

