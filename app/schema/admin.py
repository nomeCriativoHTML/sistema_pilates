from pydantic import BaseModel, EmailStr, ConfigDict
from enum import Enum
from datetime import date, datetime
from typing import Optional
from decimal import Decimal

# Enums
class Status(str, Enum):
    ativo = "ativo"
    inativo = "inativo"
    pendente = "pendente"

# ---- Dashboard ----
class DashboardBase(BaseModel):
    total_alunos: int = 0
    total_professores: int = 0
    total_estudos: int = 0
    pagamentos_em_atraso: int = 0
    alunos_hide: int = 0
    professores_hide: int = 0
    ocupacao_media: Decimal = 0.0

class DashboardCreate(DashboardBase):
    pass

class DashboardUpdate(DashboardBase):
    pass

class DashboardOut(DashboardBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

# ---- LogsDoSistema ----
class LogsDoSistemaBase(BaseModel):
    usuario: str
    acao: str
    data_hora: datetime 
    sistema_operacional: Optional[str] = None
    navegador: Optional[str] = None
    ip_address: Optional[str] = None

class LogsDoSistemaCreate(LogsDoSistemaBase):
    pass

class LogsDoSistemaUpdate(LogsDoSistemaBase):
    pass

class LogsDoSistemaOut(LogsDoSistemaBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

# ---- GestaoDeEstudos ----
class GestaoDeEstudosBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    tipo_estudo: str
    status: Optional[Status] = None
    carga_horaria: Optional[int] = 0
    total_professores: int = 0
    total_alunos: int = 0

class GestaoDeEstudosOut(GestaoDeEstudosBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

# ---- GestaoDeProfessores ----
class GestaoDeProfessoresBase(BaseModel):
    nome: str
    email: EmailStr
    telefone: Optional[str] = None
    especialidade: Optional[str] = None
    status: Optional[Status] = None
    data_cadastro: Optional[date] = None
    total_estudos: int = 0
    total_alunos: int = 0

class GestaoDeProfessoresOut(GestaoDeProfessoresBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

# ---- GestaoDeAlunos ----
class GestaoDeAlunosBase(BaseModel):
    nome: str
    email: EmailStr
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    status: Optional[Status] = None
    data_cadastro: Optional[date] = None
    total_estudos: int = 0
    total_professores: int = 0

class GestaoDeAlunosOut(GestaoDeAlunosBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

# ---- RelatoriosDeEvolucao ----
class RelatoriosDeEvolucaoBase(BaseModel):
    nome: str
    data_criacao: date
    total_estudos: int = 0
    total_professores: int = 0
    total_alunos: int = 0
    alunos_ativos: int = 0

class RelatoriosDeEvolucaoCreate(RelatoriosDeEvolucaoBase):
    pass

class RelatoriosDeEvolucaoUpdate(RelatoriosDeEvolucaoBase):
    pass

class RelatoriosDeEvolucaoOut(RelatoriosDeEvolucaoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

# ---- RelatoriosFinanceiros ----
class RelatoriosFinanceirosBase(BaseModel):
    nome: str
    data_criacao: date
    total_alunos: int = 0
    alunos_pagantes: int = 0
    alunos_inadimplentes: int = 0
    taxa_ocupacao: Decimal = 0.0

class RelatoriosFinanceirosCreate(RelatoriosFinanceirosBase):
    pass

class RelatoriosFinanceirosUpdate(RelatoriosFinanceirosBase):
    pass

class RelatoriosFinanceirosOut(RelatoriosFinanceirosBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

# ---- Classes de criação e atualização específicas ----

class GestaoDeAlunosCreate(BaseModel):
    nome: str
    email: str
    telefone: str
    status_pagamento: Optional[str] = None

class GestaoDeAlunosUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None
    status_pagamento: Optional[str] = None

class GestaoDeProfessoresCreate(BaseModel):
    nome: str
    email: str
    telefone: str
    especialidade: Optional[str] = None

class GestaoDeProfessoresUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None
    especialidade: Optional[str] = None

class GestaoDeEstudosCreate(BaseModel):
    nome: str
    endereco: str
    telefone: str

class GestaoDeEstudosUpdate(BaseModel):
    nome: Optional[str] = None
    endereco: Optional[str] = None
    telefone: Optional[str] = None