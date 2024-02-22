"""create booking_prices table

Revision ID: de40c2b4b9b6
Revises: 8df13894742f
Create Date: 2023-10-06 13:35:04.864875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de40c2b4b9b6'
down_revision = '8df13894742f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("booking_prices",
                    sa.Column("price_id", sa.Integer,
                              primary_key=True, autoincrement=True),
                    sa.Column("booking_service",
                              sa.String(100), nullable=True),
                    sa.Column("price", sa.String(255), nullable=True),
                    sa.Column("created_at", sa.DateTime, nullable=True),
                    sa.Column("updated_at", sa.DateTime, nullable=True),
                    sa.Column("deleted_at", sa.DateTime, nullable=True))


def downgrade():
    op.drop_table("booking_prices")
