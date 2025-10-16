from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime,
    DECIMAL,
    Enum,
    ForeignKey,
    Boolean
)
from sqlalchemy.orm import relationship
from app.database.connection import Base
import enum


# ---- Enums ----
class Status(enum.Enum):
    ativo = "ativo"
    inativo = "inativo"
    pendente = "pendente"


class TipoAdmin(str, enum.Enum):
    admin_completo = "admin_completo"
    recepcionista = "recepcionista"
    financeiro = "financeiro"


# ---- Tabela Principal: Admin ----
class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    senha = Column(String(100), nullable=False)
    tipo_admin = Column(Enum(TipoAdmin), default=TipoAdmin.recepcionista)
    ativo = Column(Boolean, default=True)

    # Relacionamentos
    logs = relationship("LogDoSistema", back_populates="admin", cascade="all, delete-orphan")


# ---- Dashboard ----
class Dashboard(Base):
    __tablename__ = "dashboards"

    id = Column(Integer, primary_key=True, index=True)
    total_alunos = Column(Integer, default=0)
    total_professores = Column(Integer, default=0)
    total_estudos = Column(Integer, default=0)
    pagamentos_em_atraso = Column(Integer, default=0)
    alunos_hide = Column(Integer, default=0)
    professores_hide = Column(Integer, default=0)
    ocupacao_media = Column(DECIMAL(5, 2), default=0.0)


# ---- Logs do Sistema ----
class LogDoSistema(Base):
    __tablename__ = "logs_do_sistema"

    id = Column(Integer, primary_key=True, index=True)
    admin_id = Column(Integer, ForeignKey("admins.id"), nullable=False)
    acao = Column(String(255))
    data_hora = Column(DateTime)
    sistema_operacional = Column(String(50))
    navegador = Column(String(50))
    ip_address = Column(String(45))

    admin = relationship("Admin", back_populates="logs")


# ---- Gestão de Estudos ----
class GestaoDeEstudos(Base):
    __tablename__ = "gestao_de_estudos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    descricao = Column(String(255))
    tipo_estudo = Column(String(100))
    status = Column(Enum(Status))
    carga_horaria = Column(Integer)
    total_professores = Column(Integer, default=0)
    total_alunos = Column(Integer, default=0)


# ---- Gestão de Professores ----
class GestaoDeProfessores(Base):
    __tablename__ = "gestao_de_professores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    email = Column(String(100))
    telefone = Column(String(20))
    especialidade = Column(String(100))
    status = Column(Enum(Status))
    data_cadastro = Column(Date)
    total_estudos = Column(Integer, default=0)
    total_alunos = Column(Integer, default=0)


# ---- Gestão de Alunos ----
class GestaoDeAlunos(Base):
    __tablename__ = "gestao_de_alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    email = Column(String(100))
    telefone = Column(String(20))
    endereco = Column(String(255))
    status = Column(Enum(Status))
    data_cadastro = Column(Date)
    total_estudos = Column(Integer, default=0)
    total_professores = Column(Integer, default=0)


# ---- Relatórios de Evolução ----
class RelatorioDeEvolucao(Base):
    __tablename__ = "relatorios_de_evolucao"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    data_criacao = Column(Date)
    total_estudos = Column(Integer, default=0)
    total_professores = Column(Integer, default=0)
    total_alunos = Column(Integer, default=0)
    alunos_ativos = Column(Integer, default=0)


# ---- Relatórios Financeiros ----
class RelatorioFinanceiro(Base):
    __tablename__ = "relatorios_financeiros"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50))
    data_criacao = Column(Date)
    total_alunos = Column(Integer, default=0)
    alunos_pagantes = Column(Integer, default=0)
    alunos_inadimplentes = Column(Integer, default=0)
    taxa_ocupacao = Column(DECIMAL(5, 2), default=0.0)
