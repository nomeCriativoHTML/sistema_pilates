from sqlalchemy import Column, Integer, String, DateTime, Enum, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base
from app.models.enums import TipoIdentificador, StatusAula, Presenca

# ===========================
# PROFESSOR
# ===========================
class Professor(Base):
    __tablename__ = "professores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    cref = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    senha = Column(String(100), nullable=False)
    identificador = Column(String(100))
    tipo_identificador = Column(Enum(TipoIdentificador))
    ativo = Column(Boolean, default=True)

    # Relacionamentos
    agendamentos = relationship("Agendamento", back_populates="professor", cascade="all, delete-orphan")
    evolucoes = relationship("MinhaEvolucao", back_populates="professor", cascade="all, delete-orphan")
    agendas = relationship("Agenda", back_populates="professor", cascade="all, delete-orphan")


# ===========================
# AGENDA DO PROFESSOR
# ===========================
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

    agendamentos = relationship("Agendamento", back_populates="aula", cascade="all, delete-orphan")

    professor = relationship("Professor", back_populates="agendas")
    alunos = relationship("AlunoNaAula", back_populates="agenda", cascade="all, delete-orphan")
    evolucoes = relationship("MinhaEvolucao", back_populates="agenda", cascade="all, delete-orphan")


# ===========================
# ALUNO NA AULA
# ===========================
class AlunoNaAula(Base):
    __tablename__ = "alunos_na_aula"

    id = Column(Integer, primary_key=True, index=True)
    agenda_id = Column(Integer, ForeignKey("agendas.id"), nullable=False)
    aluno_id = Column(Integer, ForeignKey("alunos.id"), nullable=False)  # Alterado de aluno_nome para FK
    presenca = Column(Enum(Presenca), default=Presenca.indefinido)
    observacoes = Column(String(255))

    agenda = relationship("Agenda", back_populates="alunos")
    aluno = relationship("Aluno")  # relacionamento com tabela principal Aluno
