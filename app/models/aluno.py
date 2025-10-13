from sqlalchemy import Column, Integer, String, Date, DateTime, Enum, Text, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base
import enum

##teste
# ENUMS

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



# TABELA PRINCIPAL - ALUNOS

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(String(20))
    email = Column(String(100), unique=True, nullable=False)
    data_nascimento = Column(Date)
    status_pagamento = Column(Enum(StatusPagamento), default=StatusPagamento.pendente)

    # Relacionamentos
    evolucoes = relationship("MinhaEvolucao", back_populates="aluno", cascade="all, delete-orphan")
    pagamentos = relationship("MeusPagamentos", back_populates="aluno", cascade="all, delete-orphan")
    agendamentos = relationship("Agendamentos", back_populates="aluno", cascade="all, delete-orphan")



# AULAS DISPONÍVEIS (GERAL)

class AulasDisponiveis(Base):
    __tablename__ = "aulas_disponiveis"

    id = Column(Integer, primary_key=True, index=True)
    data_hora = Column(DateTime, nullable=False)
    professor = Column(String(100))
    vagas = Column(Integer, default=3)
    status_agendamento = Column(Enum(StatusAgendamento), default=StatusAgendamento.disponivel)



# MINHA EVOLUÇÃO (RELACIONADO AO ALUNO)

class MinhaEvolucao(Base):
    __tablename__ = "minha_evolucao"

    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"))
    data_aula = Column(Date, nullable=False)
    professor = Column(String(100))
    exercicios_realizados = Column(Text)
    observacoes = Column(Text)
    progresso = Column(String(50))

    aluno = relationship("Aluno", back_populates="evolucoes")


# MEUS PAGAMENTOS (RELACIONADO AO ALUNO)

class MeusPagamentos(Base):
    __tablename__ = "meus_pagamentos"

    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"))
    valor = Column(DECIMAL(10, 2), nullable=False)
    data_pagamento = Column(Date, nullable=False)
    status_pagamento = Column(Enum(StatusPagamento))
    metodo_pagamento = Column(String(50))

    aluno = relationship("Aluno", back_populates="pagamentos")



# AGENDAMENTOS (RELACIONADO AO ALUNO)

class Agendamentos(Base):
    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"))
    data_hora = Column(DateTime, nullable=False)
    professor = Column(String(100))
    aula = Column(String(50))
    minha_presenca = Column(Enum(Presenca), default=Presenca.indefinido)

    aluno = relationship("Aluno", back_populates="agendamentos")
