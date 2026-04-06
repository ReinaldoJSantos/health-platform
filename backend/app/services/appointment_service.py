from sqlalchemy.orm import Session
from app.models.appointment import Appointments
from app.models.professional import Professional
from app.models.patient import Patient
from app.schemas.appointments import AppointmentCreate
from app.core.rabbitmq import publish_event


def create_appointment(db: Session, data: AppointmentCreate):
    patient = db.query(Patient).filter(Patient.id == data.paciente_id).first()
    if not patient:
        raise ValueError("Paciente não encontrado")

    professional = db.query(Professional).filter(Professional.id == data.profissional_id).first()
    if not professional:
        raise ValueError("Profissional não encontrado")

    appointment = Appointments(**data.model_dump())
    db.add(appointment)
    db.commit()
    db.refresh(appointment)

    # publicacao do evento
    publish_event(
        queue="appointment_created",
        message={
            "event": "appointment_created",
            "appointment_id": appointment.id,
            "patient_id": appointment.patient_id,
            "professional_id": appointment.professional_id
        }
    )

    return appointment

def list_appointments(db: Session):
    return db.query(Appointments).all()





