"""create refresh_token table

Revision ID: 8df13894742f
Revises: 13f1aa4e0483
Create Date: 2023-10-06 12:57:16.064218

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8df13894742f'
down_revision = '13f1aa4e0483'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("refresh_token",
                    sa.Column("token_id", sa.Integer,
                              primary_key=True, autoincrement=True),
                    sa.Column("user_id", sa.Integer, nullable=True),
                    sa.Column("token", sa.Text, nullable=True),
                    sa.Column("expired_at", sa.DateTime, nullable=True),
                    sa.Column("created_at", sa.DateTime, nullable=True),
                    sa.Column("updated_at", sa.DateTime, nullable=True),
                    sa.Column("deleted_at", sa.DateTime, nullable=True))


def downgrade():
    op.drop_table("refresh_token")
