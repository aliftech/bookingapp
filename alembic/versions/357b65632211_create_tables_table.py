"""create tables table

Revision ID: 357b65632211
Revises: b929c9bc5bc6
Create Date: 2023-10-05 10:35:12.572274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '357b65632211'
down_revision = 'b929c9bc5bc6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("tables",
                    sa.Column("table_id", sa.Integer,
                              primary_key=True, nullable=True),
                    sa.Column("table_number", sa.Integer, nullable=True),
                    sa.Column("capacity", sa.Integer, nullable=True),
                    sa.Column("table_status", sa.Enum(
                        "available", "reserved", "occupied")),
                    sa.Column("created_at", sa.DateTime, nullable=True),
                    sa.Column("updated_at", sa.DateTime, nullable=True),
                    sa.Column("deleted_at", sa.DateTime, nullable=True))


def downgrade():
    op.drop_column("tables")
