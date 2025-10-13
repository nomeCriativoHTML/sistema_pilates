"""Refatorar models mantendo dados existentes de forma segura

Revision ID: 4c76a7f6e808
Revises: dcd2e56739a6
Create Date: 2025-10-13 15:30:00
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
from sqlalchemy.engine.reflection import Inspector

revision = '4c76a7f6e808'
down_revision = 'dcd2e56739a6'
branch_labels = None
depends_on = None

def upgrade() -> None:
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)

    # === AGENDAMENTOS ===
    if 'agendamentos' in inspector.get_table_names():
        columns = [c['name'] for c in inspector.get_columns('agendamentos')]
        with op.batch_alter_table("agendamentos") as batch_op:
            if 'id' not in columns:
                batch_op.add_column(sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True))
            if 'professor' not in columns:
                batch_op.add_column(sa.Column('professor', sa.String(length=100), nullable=False))

    # === ALUNOS_NA_AULA ===
    if 'alunos_na_aula' in inspector.get_table_names():
        columns = [c['name'] for c in inspector.get_columns('alunos_na_aula')]
        with op.batch_alter_table("alunos_na_aula") as batch_op:
            if 'frequencia' not in columns:
                batch_op.add_column(sa.Column('frequencia', mysql.ENUM('presente','ausente','indefinido'), nullable=False))

    # === AULAS_DISPONIVEIS ===
    if 'aulas_disponiveis' in inspector.get_table_names():
        columns = [c['name'] for c in inspector.get_columns('aulas_disponiveis')]
        with op.batch_alter_table("aulas_disponiveis") as batch_op:
            if 'horario' not in columns:
                batch_op.add_column(sa.Column('horario', sa.String(length=20), nullable=False))
            if 'tipo_aula' not in columns:
                batch_op.add_column(sa.Column('tipo_aula', sa.String(length=50), nullable=False))

    # === MEUS_PAGAMENTOS ===
    if 'meus_pagamentos' in inspector.get_table_names():
        columns = [c['name'] for c in inspector.get_columns('meus_pagamentos')]
        with op.batch_alter_table("meus_pagamentos") as batch_op:
            if 'valor' not in columns:
                batch_op.add_column(sa.Column('valor', sa.Float(), nullable=False))
            if 'status' not in columns:
                batch_op.add_column(sa.Column('status', mysql.ENUM('pago','pendente'), nullable=False))

    # === MINHA_EVOLUCAO ===
    if 'minha_evolucao' in inspector.get_table_names():
        columns = [c['name'] for c in inspector.get_columns('minha_evolucao')]
        with op.batch_alter_table("minha_evolucao") as batch_op:
            if 'peso' not in columns:
                batch_op.add_column(sa.Column('peso', sa.Float(), nullable=False))
            if 'altura' not in columns:
                batch_op.add_column(sa.Column('altura', sa.Float(), nullable=False))
            if 'imc' not in columns:
                batch_op.add_column(sa.Column('imc', sa.Float(), nullable=True))

def downgrade() -> None:
    pass
