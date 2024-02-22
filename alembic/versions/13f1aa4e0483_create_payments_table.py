"""create payments table

Revision ID: 13f1aa4e0483
Revises: 357b65632211
Create Date: 2023-10-05 10:53:06.476395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13f1aa4e0483'
down_revision = '357b65632211'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("payments",
                    sa.Column("payment_id", sa.Integer,
                              primary_key=True, autoincrement=True),
                    sa.Column("booking_id", sa.Integer, nullable=True),
                    sa.Column("amount_payment", sa.String(255), nullable=True),
                    sa.Column("payment_method", sa.String(100), nullable=True),
                    sa.Column("created_at", sa.DateTime, nullable=True),
                    sa.Column("updated_at", sa.DateTime, nullable=True),
                    sa.Column("deleted_at", sa.DateTime, nullable=True))


def downgrade():
    op.drop_table("payments")
