from sqlalchemy import Column, Integer, String, Date, DateTime, Enum, Text, DECIMAL
from app.database.connection import Base
import enum

# Enums
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

# Tabelas

class MinhaConta(Base):
    __tablename__ = "Minha_Conta"

    oid = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50), nullable=False, unique=True)
    status_pagamento = Column(Enum(StatusPagamento))

class AulasDisponiveis(Base):
    __tablename__ = "Aulas_Disponiveis"

    oid = Column(Integer, primary_key=True, index=True)
    data_hora = Column(DateTime, nullable=False)
    professor = Column(String(100))
    vagas = Column(Integer, default=3)  # máximo de 3 alunos
    status_agendamento = Column(Enum(StatusAgendamento), default=StatusAgendamento.disponivel)

class MinhaEvolucao(Base):
    __tablename__ = "Minha_Evolucao"

    oid = Column(Integer, primary_key=True, index=True)
    data_aula = Column(Date, nullable=False)
    professor = Column(String(100))
    exercicios_realizados = Column(Text)
    observacoes = Column(Text)
    progresso = Column(String(50))

class MeusPagamentos(Base):
    __tablename__ = "Meus_Pagamentos"

    oid = Column(Integer, primary_key=True, index=True)
    valor = Column(DECIMAL(10,2), nullable=False)
    data_pagamento = Column(Date, nullable=False)
    status_pagamento = Column(Enum(StatusPagamento))
    metodo_pagamento = Column(String(50))

class Agendamentos(Base):
    __tablename__ = "Agendamentos"

    oid = Column(Integer, primary_key=True, index=True)
    data_hora = Column(DateTime, nullable=False)
    professor = Column(String(100))
    aula = Column(String(50))
    minha_presenca = Column(Enum(Presenca), default=Presenca.indefinido)
