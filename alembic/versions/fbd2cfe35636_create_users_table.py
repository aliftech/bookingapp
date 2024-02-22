"""create users table

Revision ID: fbd2cfe35636
Revises: 
Create Date: 2023-10-05 09:15:48.363281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbd2cfe35636'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
                    sa.Column("user_id", sa.Integer,
                              primary_key=True, autoincrement=True),
                    sa.Column("name", sa.String(100), nullable=True),
                    sa.Column("email", sa.String(255),
                              unique=True, nullable=False),
                    sa.Column("phone", sa.String(20), nullable=True),
                    sa.Column("address", sa.Text, nullable=True),
                    sa.Column("password", sa.Text, nullable=True))


def downgrade():
    op.drop_table("users")
