from sqlalchemy import Column, Integer, String, Date, DateTime, Enum, Boolean, Text
from app.database.connection import Base
import enum

# Enums
class TipoIdentificador(enum.Enum):
    cpf = "cpf"
    rg = "rg"
    outro = "outro"

class StatusAula(enum.Enum):
    disponivel = "disponivel"
    em_andamento = "em_andamento"
    finalizada = "finalizada"

class Presenca(enum.Enum):
    presente = "presente"
    ausente = "ausente"
    indefinido = "indefinido"

# Tabelas

class MinhaContaProfessor(Base):
    __tablename__ = "Minha_Conta_Professor"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    senha = Column(String(100), nullable=False)
    identificador = Column(String(100))
    tipo_identificador = Column(Enum(TipoIdentificador))
    professor = Column(Boolean, default=True)

class MinhaAgenda(Base):
    __tablename__ = "Minha_Agenda"

    id = Column(Integer, primary_key=True, index=True)
    data_hora = Column(DateTime, nullable=False)
    tipo_aula = Column(String(50))
    estudo = Column(String(100))
    alunos_confirmados = Column(Integer, default=0)
    max_alunos = Column(Integer, default=3)
    status = Column(Enum(StatusAula), default=StatusAula.disponivel)

class AlunosNaAula(Base):
    __tablename__ = "Alunos_na_Aula"

    agendamento_id = Column(Integer, primary_key=True)
    aula_id = Column(Integer, primary_key=True)
    aluno_nome = Column(String(100))
    presenca = Column(Enum(Presenca), default=Presenca.indefinido)
    observacoes = Column(Text)

class DadosDosAlunos(Base):
    __tablename__ = "Dados_dos_Alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(String(20))
    restricoes = Column(Text)
    interesses = Column(Text)
    evolucao = Column(Text)

