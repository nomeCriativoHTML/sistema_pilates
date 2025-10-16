"""Alterações na model do professor

Revision ID: d0d5ae17abe0
Revises: d6fb6ee6444a
Create Date: 2025-10-16 02:03:16.398691

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd0d5ae17abe0'
down_revision: Union[str, None] = 'd6fb6ee6444a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
