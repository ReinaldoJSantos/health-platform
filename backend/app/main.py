from fastapi import FastAPI
from app.core.database import engine, Base

from app.models import patient, professional
from app.api import patient



app = FastAPI(title="Healt Plataform API")
app.include_router(patient.router)


Base.metadata.create_all(bind=engine)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

