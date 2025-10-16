"""Adicionar tabela Admin e padronizar models do módulo admin

Revision ID: d6fb6ee6444a
Revises: 4c76a7f6e808
Create Date: 2025-10-16 01:37:15.539545

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd6fb6ee6444a'
down_revision: Union[str, None] = '4c76a7f6e808'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
