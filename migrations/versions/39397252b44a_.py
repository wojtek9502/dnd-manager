"""empty message

Revision ID: 39397252b44a
Revises: 40f0d28b0ce4
Create Date: 2024-01-12 20:54:50.917981

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '39397252b44a'
down_revision: Union[str, None] = '40f0d28b0ce4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('us_user',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('username', sa.String(length=512), nullable=False),
    sa.Column('password_hash', sa.LargeBinary(length=8192), nullable=False),
    sa.Column('salt', sa.LargeBinary(length=512), nullable=False),
    sa.Column('hash_algo', sa.String(length=10), nullable=False),
    sa.Column('iterations', sa.Integer(), nullable=False),
    sa.Column('inserted_on', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_on', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )

def downgrade() -> None:
    op.drop_table('us_user')