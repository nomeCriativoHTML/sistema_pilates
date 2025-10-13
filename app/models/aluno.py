from sqlalchemy import Column, Integer, String, Date, DateTime, Enum, Text, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base
import enum

# ===========================
# ENUMS
# ===========================

class StatusPagamento(enum.Enum):
    pendente = "pendente"
    pago = "pago"
    atrasado = "atrasado"


class StatusAgendamento(enum.Enum):
    disponivel = "disponivel"
    reservado = "reservado"
    cancelado = "cancelado"


class Presenca(enum.Enum):
    presente = "presente"
    ausente = "ausente"
    indefinido = "indefinido"


# ===========================
# TABELA PRINCIPAL - ALUNOS
# ===========================

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(String(20), nullable=True)
    email = Column(String(100), unique=True, nullable=False)
    data_nascimento = Column(Date, nullable=True)
    status_pagamento = Column(Enum(StatusPagamento, name="status_pagamento_enum"), default=StatusPagamento.pendente, nullable=False)

    # Relacionamentos
    evolucoes = relationship("MinhaEvolucao", back_populates="aluno", cascade="all, delete-orphan")
    pagamentos = relationship("MeusPagamentos", back_populates="aluno", cascade="all, delete-orphan")
    agendamentos = relationship("Agendamento", back_populates="aluno", cascade="all, delete-orphan")


# ===========================
# AULAS DISPONÍVEIS (GERAL)
# ===========================

class AulasDisponiveis(Base):
    __tablename__ = "aulas_disponiveis"

    id = Column(Integer, primary_key=True, index=True)
    data_hora = Column(DateTime, nullable=False)
    professor = Column(String(100), nullable=False)
    vagas = Column(Integer, default=3, nullable=False)
    status_agendamento = Column(Enum(StatusAgendamento, name="status_agendamento_enum"), default=StatusAgendamento.disponivel, nullable=False)


# ===========================
# MINHA EVOLUÇÃO (RELACIONADO AO ALUNO)
# ===========================

class MinhaEvolucao(Base):
    __tablename__ = "minha_evolucao"

    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"), nullable=False)
    data_aula = Column(Date, nullable=False)
    professor = Column(String(100), nullable=False)
    exercicios_realizados = Column(Text, nullable=True)
    observacoes = Column(Text, nullable=True)
    progresso = Column(String(50), nullable=True)

    aluno = relationship("Aluno", back_populates="evolucoes")


# ===========================
# MEUS PAGAMENTOS (RELACIONADO AO ALUNO)
# ===========================

class MeusPagamentos(Base):
    __tablename__ = "meus_pagamentos"

    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"), nullable=False)
    valor = Column(DECIMAL(10, 2), nullable=False)
    data_pagamento = Column(Date, nullable=False)
    status_pagamento = Column(Enum(StatusPagamento, name="status_pagamento_enum"), default=StatusPagamento.pendente, nullable=False)
    metodo_pagamento = Column(String(50), nullable=False)

    aluno = relationship("Aluno", back_populates="pagamentos")


# ===========================
# AGENDAMENTOS (RELACIONADO AO ALUNO)
# ===========================

class Agendamento(Base):
    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"), nullable=False)
    data_hora = Column(DateTime, nullable=False)
    professor = Column(String(100), nullable=False)
    aula = Column(String(50), nullable=False)
    minha_presenca = Column(Enum(Presenca, name="presenca_enum"), default=Presenca.indefinido, nullable=False)

    aluno = relationship("Aluno", back_populates="agendamentos")
