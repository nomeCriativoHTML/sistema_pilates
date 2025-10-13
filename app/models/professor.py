from sqlalchemy import Column, Integer, String, Date, DateTime, Enum, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base
import enum

# ---- Enums ----
class TipoIdentificador(str, enum.Enum):
    cpf = "cpf"
    rg = "rg"
    outro = "outro"

class StatusAula(str, enum.Enum):
    disponivel = "disponivel"
    em_andamento = "em_andamento"
    finalizada = "finalizada"

class Presenca(str, enum.Enum):
    presente = "presente"
    ausente = "ausente"
    indefinido = "indefinido"

# ---- Tabela Principal: Professor ----
class Professor(Base):
    __tablename__ = "professores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    senha = Column(String(100), nullable=False)
    identificador = Column(String(100))
    tipo_identificador = Column(Enum(TipoIdentificador))
    ativo = Column(Boolean, default=True)

    # Relacionamentos
    pagamentos = relationship("Pagamento", back_populates="professor", cascade="all, delete-orphan")
    evolucao = relationship("EvolucaoAluno", back_populates="professor", cascade="all, delete-orphan")
    agendas = relationship("Agenda", back_populates="professor", cascade="all, delete-orphan")

# ---- Agenda do Professor ----
class Agenda(Base):
    __tablename__ = "agendas"

    id = Column(Integer, primary_key=True, index=True)
    professor_id = Column(Integer, ForeignKey("professores.id"), nullable=False)
    data_hora = Column(DateTime, nullable=False)
    tipo_aula = Column(String(50))
    estudo = Column(String(100))
    alunos_confirmados = Column(Integer, default=0)
    max_alunos = Column(Integer, default=3)
    status = Column(Enum(StatusAula), default=StatusAula.disponivel)

    professor = relationship("Professor", back_populates="agendas")
    alunos = relationship("AlunoNaAula", back_populates="agenda", cascade="all, delete-orphan")

# ---- Alunos na Aula ----
class AlunoNaAula(Base):
    __tablename__ = "alunos_na_aula"

    id = Column(Integer, primary_key=True, index=True)
    agenda_id = Column(Integer, ForeignKey("agendas.id"), nullable=False)
    aluno_nome = Column(String(100))
    presenca = Column(Enum(Presenca), default=Presenca.indefinido)
    observacoes = Column(Text)

    agenda = relationship("Agenda", back_populates="alunos")

# ---- Dados dos Alunos ----
class DadosAluno(Base):
    __tablename__ = "dados_dos_alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(String(20))
    restricoes = Column(Text)
    interesses = Column(Text)
    evolucao = Column(Text)
