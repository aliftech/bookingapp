from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime
from core.config.database import Base


class PaymentModel(Base):
    __tablename__ = "payments"
    payment_id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer)
    amount_payment = Column(String)
    payment_method = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
