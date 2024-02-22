from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.table.schema.table_schema import CreateTable
from core.config.database import get_db
from app.table.controller.table_controller import create


table = APIRouter()


class Table:

    @table.post("/table")
    def create_table(table: CreateTable, session: Session = Depends(get_db)):
        data = create(session, table)
        return data
