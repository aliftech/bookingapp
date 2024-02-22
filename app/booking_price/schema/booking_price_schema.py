from fastapi import Form
from pydantic import BaseModel


class CreateBookPrice(BaseModel):
    booking_service: str = Form(...)
    price: str = Form(...)


class BookPriceList(CreateBookPrice):
    price_id: int

    class Config:
        orm_mode = True
