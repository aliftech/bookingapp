from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime
from core.config.database import Base


class BookingPriceModel(Base):
    __tablename__ = "booking_prices"
    price_id = Column(Integer, primary_key=True, index=True)
    booking_service = Column(String)
    price = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
