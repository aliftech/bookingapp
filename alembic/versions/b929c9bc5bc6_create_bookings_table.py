"""create bookings table

Revision ID: b929c9bc5bc6
Revises: d5d4fa9bc40d
Create Date: 2023-10-05 10:25:23.123098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b929c9bc5bc6'
down_revision = 'd5d4fa9bc40d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("bookings",
                    sa.Column("booking_id", sa.Integer,
                              primary_key=True, autoincrement=True),
                    sa.Column("user_id", sa.Integer, nullable=True),
                    sa.Column("table_id", sa.Integer, nullable=True),
                    sa.Column("booking_date", sa.String(100), nullable=True),
                    sa.Column("booking_time", sa.String(100), nullable=True),
                    sa.Column("number_of_guest", sa.Integer, nullable=True),
                    sa.Column("booking_status", sa.Enum(
                        "pending", "approved", "canceled", "rejected")),
                    sa.Column("created_at", sa.DateTime, nullable=True),
                    sa.Column("updated_at", sa.DateTime, nullable=True),
                    sa.Column("deleted_at", sa.DateTime, nullable=True))


def downgrade():
    op.drop_table("bookings")
