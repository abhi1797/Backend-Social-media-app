"""add content column to post table

Revision ID: e3e9381eb688
Revises: 537af8895618
Create Date: 2025-01-27 11:15:39.235678

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e3e9381eb688'
down_revision: Union[str, None] = '537af8895618'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content',sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
