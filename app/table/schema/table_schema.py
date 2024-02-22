from fastapi import Form
from pydantic import BaseModel


class CreateTable(BaseModel):
    table_number: int = Form(...)
    capacity: int = Form(...)


class Table(CreateTable):
    table_id: int

    class Config:
        orm_mode = True
