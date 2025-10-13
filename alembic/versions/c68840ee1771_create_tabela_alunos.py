"""create tabela alunos

Revision ID: c68840ee1771
Revises: b3f2140c23a6
Create Date: 2025-10-13 14:28:13.448627

"""
from alembic import op
import sqlalchemy as sa
import enum

# ENUMS devem ser recriados aqui
class StatusPagamentoEnum(enum.Enum):
    pendente = "pendente"
    pago = "pago"
    atrasado = "atrasado"

# revision identifiers, used by Alembic.
revision = 'xxxx_create_alunos'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Criação da tabela alunos
    op.create_table(
        'alunos',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('nome', sa.String(100), nullable=False),
        sa.Column('telefone', sa.String(20), nullable=True),
        sa.Column('email', sa.String(100), nullable=False, unique=True),
        sa.Column('data_nascimento', sa.Date, nullable=True),
        sa.Column('status_pagamento', sa.Enum(StatusPagamentoEnum), nullable=False, server_default="pendente")
    )

def downgrade():
    op.drop_table('alunos')
