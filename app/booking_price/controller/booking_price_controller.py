from datetime import datetime
from app.booking_price.model.booking_price_model import BookingPriceModel
from core.helper.response_helper import ResponseData


def create(session, booking_price) -> ResponseData:
    current_time = datetime.now()
    new_booking_price = BookingPriceModel(
        booking_service=booking_price.booking_service,
        price=booking_price.price,
        created_at=current_time
    )

    session.add(new_booking_price)
    session.commit()

    return ResponseData(status_code=200, message="Booking price created successfully.")
