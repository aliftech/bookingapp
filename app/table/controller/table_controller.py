from datetime import datetime
from app.table.model.table_model import TableModel
from core.helper.response_helper import ResponseData


def create(session, table) -> ResponseData:
    current_time = datetime.now()
    new_table = TableModel(
        table_number=table.table_number,
        capacity=table.capacity,
        table_status='available',
        created_at=current_time
    )

    session.add(new_table)
    session.commit()

    return ResponseData(status_code=200, message="New table created successfully.")
