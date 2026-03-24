from fastapi import FastAPI
from app.core.database import engine, Base

from app.core.database import patinent

app = FastAPI(title="Healt Plataform API")

Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}