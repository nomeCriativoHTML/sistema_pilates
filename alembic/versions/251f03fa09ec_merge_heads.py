"""merge heads

Revision ID: 251f03fa09ec
Revises: b3f2140c23a6, xxxx_create_alunos
Create Date: 2025-10-13 14:34:43.047973

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '251f03fa09ec'
down_revision: Union[str, None] = ('b3f2140c23a6', 'xxxx_create_alunos')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
