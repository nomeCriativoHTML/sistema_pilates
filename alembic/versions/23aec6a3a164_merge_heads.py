"""merge heads

Revision ID: 23aec6a3a164
Revises: 6374cef99c93, 251f03fa09ec
Create Date: 2025-10-13 15:05:25.621339

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '23aec6a3a164'
down_revision: Union[str, None] = ('6374cef99c93', '251f03fa09ec')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
