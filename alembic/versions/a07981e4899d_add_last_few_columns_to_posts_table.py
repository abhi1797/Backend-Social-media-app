"""add last few columns to posts table

Revision ID: a07981e4899d
Revises: 1a8dac553147
Create Date: 2025-01-27 14:37:23.166165

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a07981e4899d'
down_revision: Union[str, None] = '1a8dac553147'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='True'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)

    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts', 'created_at')
    pass
