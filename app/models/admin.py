from sqlalchemy import Column, Integer, String, Date, DateTime, DECIMAL, Enum
from app.database.connection import Base
import enum

# Enums
class Status(enum.Enum):
    ativo = "ativo"
    inativo = "inativo"
    pendente = "pendente"

# Tabelas

class Dashboard(Base):
    __tablename__ = "Dashboard"

    id = Column(Integer, primary_key=True, index=True)
    total_alunos = Column(Integer, default=0)
    total_professores = Column(Integer, default=0)
    total_estudos = Column(Integer, default=0)
    pagamentos_em_atraso = Column(Integer, default=0)
    alunos_hide = Column(Integer, default=0)
    professores_hide = Column(Integer, default=0)
    ocupacao_media = Column(DECIMAL(5,2), default=0.0)

class LogsDoSistema(Base):
    __tablename__ = "Logs_do_Sistema"

    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String(100))
    acao = Column(String(100))
    data_hora = Column(DateTime)
    sistema_operacional = Column(String(50))
    navegador = Column(String(50))
    ip_address = Column(String(45))

class GestaoDeEstudos(Base):
    __tablename__ = "Gestao_de_Estudos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    descricao = Column(String(255))
    tipo_estudo = Column(String(100))
    status = Column(Enum(Status))
    carga_horaria = Column(Integer)
    total_professores = Column(Integer, default=0)
    total_alunos = Column(Integer, default=0)

class GestaoDeProfessores(Base):
    __tablename__ = "Gestao_de_Professores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    email = Column(String(100))
    telefone = Column(String(20))
    especialidade = Column(String(100))
    status = Column(Enum(Status))
    data_cadastro = Column(Date)
    total_estudos = Column(Integer, default=0)
    total_alunos = Column(Integer, default=0)

class GestaoDeAlunos(Base):
    __tablename__ = "Gestao_de_Alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    email = Column(String(100))
    telefone = Column(String(20))
    endereco = Column(String(255))
    status = Column(Enum(Status))
    data_cadastro = Column(Date)
    total_estudos = Column(Integer, default=0)
    total_professores = Column(Integer, default=0)

class RelatoriosDeEvolucao(Base):
    __tablename__ = "Relatorios_de_Evolucao"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    data_criacao = Column(Date)
    total_estudos = Column(Integer, default=0)
    total_professores = Column(Integer, default=0)
    total_alunos = Column(Integer, default=0)
    alunos_ativos = Column(Integer, default=0)

class RelatoriosFinanceiros(Base):
    __tablename__ = "Relatorios_Financeiros"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50))
    data_criacao = Column(Date)
    total_alunos = Column(Integer, default=0)
    alunos_pagantes = Column(Integer, default=0)
    alunos_inadimplentes = Column(Integer, default=0)
    taxa_ocupacao = Column(DECIMAL(5,2), default=0.0)
