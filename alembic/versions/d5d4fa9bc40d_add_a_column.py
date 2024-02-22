"""Add a column

Revision ID: d5d4fa9bc40d
Revises: fbd2cfe35636
Create Date: 2023-10-05 09:29:45.201768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5d4fa9bc40d'
down_revision = 'fbd2cfe35636'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users", sa.Column("created_at", sa.DateTime, nullable=True))
    op.add_column("users", sa.Column("updated_at", sa.DateTime, nullable=True))
    op.add_column("users", sa.Column("deleted_at", sa.DateTime, nullable=True))


def downgrade():
    op.drop_column("users", "created_at")
    op.drop_column("users", "updated_at")
    op.drop_column("users", "deleted_at")
