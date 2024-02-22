from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime, Time, Date
from core.config.database import Base


class BookingModel(Base):
    __tablename__ = "bookings"
    booking_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    table_id = Column(Integer)
    booking_date = Column(Date)
    booking_time = Column(Time)
    number_of_guest = Column(Integer)
    booking_status = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
