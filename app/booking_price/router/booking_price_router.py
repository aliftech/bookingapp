from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.booking_price.schema.booking_price_schema import CreateBookPrice
from core.config.database import get_db
from app.booking_price.controller.booking_price_controller import create


price = APIRouter()


class BookingPrice:

    @price.post("/booking-price")
    def create_booking_price(booking_price: CreateBookPrice, session: Session = Depends(get_db)):
        data = create(session, booking_price)
        return data
