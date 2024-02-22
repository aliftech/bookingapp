from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.registration.controller.registration_controller import create
from core.config.database import get_db
from app.registration.schema.registration_schema import CreateRegistration

registration = APIRouter()


class RegistrationRouter:
    @registration.post("/registration")
    def create(data: CreateRegistration, session: Session = Depends(get_db)):
        registration = create(session, data)
        return registration
