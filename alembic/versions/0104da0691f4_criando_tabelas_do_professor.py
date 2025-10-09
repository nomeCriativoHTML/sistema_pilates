"""Criando tabelas do professor

Revision ID: 0104da0691f4
Revises: 95e83869bb7c
Create Date: 2025-10-09 01:56:22.559026
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '0104da0691f4'
down_revision: Union[str, None] = '95e83869bb7c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Criar tabela Minha_Conta_Professor
    op.create_table(
        'Minha_Conta_Professor',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('nome', sa.String(length=100), nullable=False),
        sa.Column('email', sa.String(length=100), nullable=False, unique=True),
        sa.Column('senha', sa.String(length=100), nullable=False),
        sa.Column('identificador', sa.String(length=100), nullable=True),
        sa.Column('tipo_identificador', sa.Enum('cpf', 'rg', 'outro', name='tipoidentificador'), nullable=True),
        sa.Column('professor', sa.Boolean(), default=True, nullable=True)
    )

    # Criar tabela Minha_Agenda
    op.create_table(
        'Minha_Agenda',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('data_hora', sa.DateTime(), nullable=False),
        sa.Column('tipo_aula', sa.String(length=50), nullable=True),
        sa.Column('estudo', sa.String(length=100), nullable=True),
        sa.Column('alunos_confirmados', sa.Integer(), default=0, nullable=True),
        sa.Column('max_alunos', sa.Integer(), default=3, nullable=True),
        sa.Column('status', sa.Enum('disponivel', 'em_andamento', 'finalizada', name='statusaula'), default='disponivel', nullable=True)
    )

    # Criar tabela Alunos_na_Aula
    op.create_table(
        'Alunos_na_Aula',
        sa.Column('agendamento_id', sa.Integer(), primary_key=True),
        sa.Column('aula_id', sa.Integer(), primary_key=True),
        sa.Column('aluno_nome', sa.String(length=100), nullable=True),
        sa.Column('presenca', sa.Enum('presente', 'ausente', 'indefinido', name='presenca'), default='indefinido', nullable=True),
        sa.Column('observacoes', sa.Text(), nullable=True)
    )

    # Criar tabela Dados_dos_Alunos
    op.create_table(
        'Dados_dos_Alunos',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('nome', sa.String(length=100), nullable=False),
        sa.Column('telefone', sa.String(length=20), nullable=True),
        sa.Column('restricoes', sa.Text(), nullable=True),
        sa.Column('interesses', sa.Text(), nullable=True),
        sa.Column('evolucao', sa.Text(), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('Dados_dos_Alunos')
    op.drop_table('Alunos_na_Aula')
    op.drop_table('Minha_Agenda')
    op.drop_table('Minha_Conta_Professor')
