from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum, DateTime, Text
from core.config.database import Base


class RefreshToken(Base):
    __tablename__ = "refresh_token"
    token_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    token = Column(Text)
    expired_at = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
