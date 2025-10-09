from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import datetime
from typing import Optional

# Enums
class TipoIdentificador(str, Enum):
    cpf = "cpf"
    rg = "rg"
    outro = "outro"

class StatusAula(str, Enum):
    disponivel = "disponivel"
    em_andamento = "em_andamento"
    finalizada = "finalizada"

class Presenca(str, Enum):
    presente = "presente"
    ausente = "ausente"
    indefinido = "indefinido"

# ---- MinhaContaProfessor ----
class MinhaContaProfessorBase(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    identificador: Optional[str] = None
    tipo_identificador: Optional[TipoIdentificador] = None
    professor: Optional[bool] = True

class MinhaContaProfessorCreate(MinhaContaProfessorBase):
    pass

class MinhaContaProfessorUpdate(MinhaContaProfessorBase):
    pass

class MinhaContaProfessorOut(MinhaContaProfessorBase):
    id: int

    class Config:
        orm_mode = True

# ---- MinhaAgenda ----
class MinhaAgendaBase(BaseModel):
    data_hora: datetime
    tipo_aula: str
    estudo: str
    alunos_confirmados: int = 0
    max_alunos: int = 3
    status: Optional[StatusAula] = StatusAula.disponivel

class MinhaAgendaCreate(MinhaAgendaBase):
    pass

class MinhaAgendaUpdate(MinhaAgendaBase):
    pass

class MinhaAgendaOut(MinhaAgendaBase):
    id: int

    class Config:
        orm_mode = True

# ---- AlunosNaAula ----
class AlunosNaAulaBase(BaseModel):
    agendamento_id: int
    aula_id: int
    aluno_nome: str
    presenca: Optional[Presenca] = Presenca.indefinido
    observacoes: Optional[str] = None

class AlunosNaAulaCreate(AlunosNaAulaBase):
    pass

class AlunosNaAulaUpdate(AlunosNaAulaBase):
    pass

class AlunosNaAulaOut(AlunosNaAulaBase):
    class Config:
        orm_mode = True

# ---- DadosDosAlunos ----
class DadosDosAlunosBase(BaseModel):
    nome: str
    telefone: Optional[str] = None
    restricoes: Optional[str] = None
    interesses: Optional[str] = None
    evolucao: Optional[str] = None

class DadosDosAlunosCreate(DadosDosAlunosBase):
    pass

class DadosDosAlunosUpdate(DadosDosAlunosBase):
    pass

class DadosDosAlunosOut(DadosDosAlunosBase):
    id: int

    class Config:
        orm_mode = True
