"""empty message

Revision ID: 40f0d28b0ce4
Revises: 
Create Date: 2024-01-12 20:29:11.268282

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '40f0d28b0ce4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('cr_user',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('inserted_on', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_on', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('cr_user')
