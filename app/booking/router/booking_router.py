from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.booking.schema.ticket_schema import CreateTicket
from core.config.database import get_db
from app.booking.controller.booking_controller import booking_table, buy_ticket
from core.auth.bearer import JWTBearer

booking = APIRouter()


class Ticket:

    @booking.post("/booking/ticket")
    def book_ticket(data: CreateTicket, session: Session = Depends(get_db), token: str = Depends(JWTBearer())):
        result = buy_ticket(session, data, token)
        return result

    @booking.post("/booking/table")
    def book_ticket(data: CreateTicket, session: Session = Depends(get_db), token: str = Depends(JWTBearer())):
        result = booking_table(session, data, token)
        return result
