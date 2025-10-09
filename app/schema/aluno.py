from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import datetime, date
from typing import Optional

# Enums
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

# Schemas

# ---- MinhaConta ----
class MinhaContaBase(BaseModel):
    nome: str
    telefone: Optional[str] = None
    email: EmailStr
    status_pagamento: Optional[StatusPagamento] = None

class MinhaContaCreate(MinhaContaBase):
    pass

class MinhaContaUpdate(MinhaContaBase):
    pass

class MinhaContaOut(MinhaContaBase):
    oid: int

    class Config:
        orm_mode = True

# ---- AulasDisponiveis ----
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

    class Config:
        orm_mode = True

# ---- MinhaEvolucao ----
class MinhaEvolucaoBase(BaseModel):
    data_aula: date
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

    class Config:
        orm_mode = True

# ---- MeusPagamentos ----
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

    class Config:
        orm_mode = True

# ---- Agendamentos ----
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

    class Config:
        orm_mode = True
