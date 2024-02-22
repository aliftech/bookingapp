from datetime import datetime
from app.booking.model.booking_model import BookingModel
from app.booking.model.payment_model import PaymentModel
from app.booking_price.model.booking_price_model import BookingPriceModel
from app.table.model.table_model import TableModel
from core.helper.response_helper import ResponseData
from core.auth.token import decodeJWT


def buy_ticket(session, data, token) -> ResponseData:

    decoded_token = decodeJWT(token)
    if not decoded_token:
        return ResponseData(status_code=400, message="Invalid or expired token.")

    user_id = decoded_token.get("user_id")
    current_time = datetime.now()

    booking_price = session.query(BookingPriceModel).filter(
        BookingPriceModel.booking_service == 'ticket').first()

    if booking_price is None:
        return ResponseData(status_code=201, message="Booking failed.", data=None)

    if int(data.amount_payment) < int(40 * int(booking_price.price) / 100):
        return ResponseData(status_code=201, message="The payment amount must bigger or equal to 40 percent of ticket price.", data=None)

    tables = session.query(TableModel).filter(
        TableModel.table_number == data.table_number).first()

    if tables is not None:
        if data.guest_number > tables.capacity:
            return ResponseData(status_code=201, message="The guest number is bigger than table capacity. Please looking for another table.", data=None)
        table_id = tables.table_id
        new_booking = BookingModel(
            user_id=user_id,
            table_id=table_id,
            booking_date=data.booking_date,
            booking_time=data.booking_time,
            number_of_guest=data.guest_number,
            booking_status='pending',
            created_at=current_time
        )
        session.add(new_booking)
        session.flush()

        # Get the booking ID of the inserted data.
        booking_id = new_booking.booking_id
        new_payment = PaymentModel(
            booking_id=booking_id,
            amount_payment=data.amount_payment,
            payment_method=data.payment_method,
            created_at=current_time
        )

        session.add(new_payment)
        session.commit()

        return ResponseData(status_code=200, message="Booking created successfully.", data=None)


def booking_table(session, data, token) -> ResponseData:

    decoded_token = decodeJWT(token)
    if not decoded_token:
        return ResponseData(status_code=400, message="Invalid or expired token.")

    user_id = decoded_token.get("user_id")
    current_time = datetime.now()

    booking_price = session.query(BookingPriceModel).filter(
        BookingPriceModel.booking_service == 'booking').first()

    if booking_price is None:
        return ResponseData(status_code=201, message="Booking failed.", data=None)

    if int(data.amount_payment) < int(booking_price.price):
        return ResponseData(status_code=201, message="The payment amount must equal to booking price.", data=None)

    tables = session.query(TableModel).filter(
        TableModel.table_number == data.table_number).first()

    if tables is not None:
        if data.guest_number > tables.capacity:
            return ResponseData(status_code=201, message="The guest number is bigger than table capacity. Please looking for another table.", data=None)
        table_id = tables.table_id
        new_booking = BookingModel(
            user_id=user_id,
            table_id=table_id,
            booking_date=data.booking_date,
            booking_time=data.booking_time,
            number_of_guest=data.guest_number,
            booking_status='pending',
            created_at=current_time
        )
        session.add(new_booking)
        session.flush()

        # Get the booking ID of the inserted data.
        booking_id = new_booking.booking_id
        new_payment = PaymentModel(
            booking_id=booking_id,
            amount_payment=data.amount_payment,
            payment_method=data.payment_method,
            created_at=current_time
        )

        session.add(new_payment)
        session.commit()

        return ResponseData(status_code=200, message="Booking created successfully.", data=None)
