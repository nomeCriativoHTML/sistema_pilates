from pydantic import BaseModel, EmailStr, ConfigDict
from enum import Enum
from datetime import datetime, date
from typing import Optional

# ===========================
# ENUMS
# ===========================
class StatusPagamento(str, Enum):
    pendente = "pendente"
    pago = "pago"
    atrasado = "atrasado"

class StatusAgendamento(str, Enum):
    disponivel = "disponivel"
    reservado = "reservado"
    cancelado = "cancelado"

class Presenca(str, Enum):
    presente = "presente"
    ausente = "ausente"
    indefinido = "indefinido"

# ===========================
# ALUNO
# ===========================
class AlunoBase(BaseModel):
    nome: str
    telefone: Optional[str] = None
    email: EmailStr
    data_nascimento: Optional[date] = None
    status_pagamento: StatusPagamento = StatusPagamento.pendente

class AlunoCreate(AlunoBase):
    cpf: str
    senha: str

class AlunoUpdate(AlunoBase):
    cpf: Optional[str] = None
    senha: Optional[str] = None

class AlunoOut(AlunoBase):
    id: int
    cpf: str

    model_config = ConfigDict(from_attributes=True)

# ===========================
# AULAS DISPONIVEIS
# ===========================
class AulasDisponiveisBase(BaseModel):
    data_hora: datetime
    professor: str
    vagas: int
    status_agendamento: Optional[StatusAgendamento] = StatusAgendamento.disponivel

class AulasDisponiveisCreate(AulasDisponiveisBase):
    pass

class AulasDisponiveisUpdate(AulasDisponiveisBase):
    pass

class AulasDisponiveisOut(AulasDisponiveisBase):
    oid: int

    model_config = ConfigDict(from_attributes=True)

# ===========================
# MINHA EVOLUÇÃO
# ===========================
class MinhaEvolucaoBase(BaseModel):
    data_aula: datetime
    professor: str
    exercicios_realizados: Optional[str] = None
    observacoes: Optional[str] = None
    progresso: Optional[str] = None

class MinhaEvolucaoCreate(MinhaEvolucaoBase):
    pass

class MinhaEvolucaoUpdate(MinhaEvolucaoBase):
    pass

class MinhaEvolucaoOut(MinhaEvolucaoBase):
    oid: int

    model_config = ConfigDict(from_attributes=True)

# ===========================
# MEUS PAGAMENTOS
# ===========================
class MeusPagamentosBase(BaseModel):
    valor: float
    data_pagamento: date
    status_pagamento: Optional[StatusPagamento] = None
    metodo_pagamento: Optional[str] = None

class MeusPagamentosCreate(MeusPagamentosBase):
    pass

class MeusPagamentosUpdate(MeusPagamentosBase):
    pass

class MeusPagamentosOut(MeusPagamentosBase):
    oid: int

    model_config = ConfigDict(from_attributes=True)

# ===========================
# AGENDAMENTOS
# ===========================
class AgendamentosBase(BaseModel):
    data_hora: datetime
    professor: str
    aula: str
    minha_presenca: Optional[Presenca] = Presenca.indefinido

class AgendamentosCreate(AgendamentosBase):
    pass

class AgendamentosUpdate(AgendamentosBase):
    pass

class AgendamentosOut(AgendamentosBase):
    oid: int

    model_config = ConfigDict(from_attributes=True)
