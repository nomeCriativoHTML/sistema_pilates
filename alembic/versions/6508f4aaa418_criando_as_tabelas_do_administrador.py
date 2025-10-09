"""Criando as tabelas do administrador

Revision ID: 6508f4aaa418
Revises: 8b63da81ab99
Create Date: 2025-10-09 02:09:49.324231
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '6508f4aaa418'
down_revision: Union[str, None] = '8b63da81ab99'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### Criação das tabelas do administrador ###
    op.create_table(
        'Dashboard',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('total_alunos', sa.Integer(), nullable=True),
        sa.Column('total_professores', sa.Integer(), nullable=True),
        sa.Column('total_estudos', sa.Integer(), nullable=True),
        sa.Column('pagamentos_em_atraso', sa.Integer(), nullable=True),
        sa.Column('alunos_hide', sa.Integer(), nullable=True),
        sa.Column('professores_hide', sa.Integer(), nullable=True),
        sa.Column('ocupacao_media', sa.DECIMAL(precision=5, scale=2), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Dashboard_id'), 'Dashboard', ['id'], unique=False)

    op.create_table(
        'Gestao_de_Alunos',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nome', sa.String(length=100), nullable=True),
        sa.Column('email', sa.String(length=100), nullable=True),
        sa.Column('telefone', sa.String(length=20), nullable=True),
        sa.Column('endereco', sa.String(length=255), nullable=True),
        sa.Column('status', sa.Enum('ativo', 'inativo', 'pendente', name='status'), nullable=True),
        sa.Column('data_cadastro', sa.Date(), nullable=True),
        sa.Column('total_estudos', sa.Integer(), nullable=True),
        sa.Column('total_professores', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Gestao_de_Alunos_id'), 'Gestao_de_Alunos', ['id'], unique=False)

    op.create_table(
        'Gestao_de_Estudos',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nome', sa.String(length=100), nullable=True),
        sa.Column('descricao', sa.String(length=255), nullable=True),
        sa.Column('tipo_estudo', sa.String(length=100), nullable=True),
        sa.Column('status', sa.Enum('ativo', 'inativo', 'pendente', name='status'), nullable=True),
        sa.Column('carga_horaria', sa.Integer(), nullable=True),
        sa.Column('total_professores', sa.Integer(), nullable=True),
        sa.Column('total_alunos', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Gestao_de_Estudos_id'), 'Gestao_de_Estudos', ['id'], unique=False)

    op.create_table(
        'Gestao_de_Professores',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nome', sa.String(length=100), nullable=True),
        sa.Column('email', sa.String(length=100), nullable=True),
        sa.Column('telefone', sa.String(length=20), nullable=True),
        sa.Column('especialidade', sa.String(length=100), nullable=True),
        sa.Column('status', sa.Enum('ativo', 'inativo', 'pendente', name='status'), nullable=True),
        sa.Column('data_cadastro', sa.Date(), nullable=True),
        sa.Column('total_estudos', sa.Integer(), nullable=True),
        sa.Column('total_alunos', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Gestao_de_Professores_id'), 'Gestao_de_Professores', ['id'], unique=False)

    op.create_table(
        'Logs_do_Sistema',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('usuario', sa.String(length=100), nullable=True),
        sa.Column('acao', sa.String(length=100), nullable=True),
        sa.Column('data_hora', sa.DateTime(), nullable=True),
        sa.Column('sistema_operacional', sa.String(length=50), nullable=True),
        sa.Column('navegador', sa.String(length=50), nullable=True),
        sa.Column('ip_address', sa.String(length=45), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Logs_do_Sistema_id'), 'Logs_do_Sistema', ['id'], unique=False)


def downgrade() -> None:
    # ### Remover apenas as tabelas do administrador ###
    op.drop_index(op.f('ix_Logs_do_Sistema_id'), table_name='Logs_do_Sistema')
    op.drop_table('Logs_do_Sistema')

    op.drop_index(op.f('ix_Gestao_de_Professores_id'), table_name='Gestao_de_Professores')
    op.drop_table('Gestao_de_Professores')

    op.drop_index(op.f('ix_Gestao_de_Estudos_id'), table_name='Gestao_de_Estudos')
    op.drop_table('Gestao_de_Estudos')

    op.drop_index(op.f('ix_Gestao_de_Alunos_id'), table_name='Gestao_de_Alunos')
    op.drop_table('Gestao_de_Alunos')

    op.drop_index(op.f('ix_Dashboard_id'), table_name='Dashboard')
    op.drop_table('Dashboard')
