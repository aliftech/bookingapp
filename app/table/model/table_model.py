from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, DateTime, String
from core.config.database import Base
import enum


class TableStatus(str, enum.Enum):
    available = "available"
    reserved = "reserved"
    occupied = "occupied"


class TableModel(Base):
    __tablename__ = "tables"
    table_id = Column(Integer, primary_key=True, index=True)
    table_number = Column(Integer)
    capacity = Column(Integer)
    table_status = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
