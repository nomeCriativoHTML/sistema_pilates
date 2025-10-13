"""merge heads

Revision ID: 6374cef99c93
Revises: 251f03fa09ec
Create Date: 2025-10-13 14:39:25.577267

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6374cef99c93'
down_revision: tuple = ('b3f2140c23a6', 'xxxx_create_alunos')  # <- CORRIGIDO
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass  # merge, nada a fazer


def downgrade() -> None:
    pass  # merge, nada a fazer

