from fastapi import Form
from pydantic import BaseModel


class CreateTicket(BaseModel):
    table_number: int = Form(...)
    guest_number: int = Form(...)
    booking_date: str = Form(...)
    booking_time: str = Form(...)
    amount_payment: str = Form(...)
    payment_method: str = Form(...)


class Ticket(CreateTicket):
    booking_id: int

    class Config:
        orm_mode = True
