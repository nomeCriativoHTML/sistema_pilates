from pydantic import BaseModel, EmailStr, ConfigDict
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

# Schemas atualizados para Pydantic V2

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

    model_config = ConfigDict(from_attributes=True)  # Atualizado para Pydantic V2

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

    model_config = ConfigDict(from_attributes=True)

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

    model_config = ConfigDict(from_attributes=True)

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

    model_config = ConfigDict(from_attributes=True)

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

    model_config = ConfigDict(from_attributes=True)