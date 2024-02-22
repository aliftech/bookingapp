from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text, DateTime
from core.config.database import Base


class Registration(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(Text)
    password = Column(Text)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
