from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import date
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

    class Config:
        orm_mode = True

# ---- LogsDoSistema ----
class LogsDoSistemaBase(BaseModel):
    usuario: str
    acao: str
    data_hora: date
    sistema_operacional: Optional[str] = None
    navegador: Optional[str] = None
    ip_address: Optional[str] = None

class LogsDoSistemaCreate(LogsDoSistemaBase):
    pass

class LogsDoSistemaUpdate(LogsDoSistemaBase):
    pass

class LogsDoSistemaOut(LogsDoSistemaBase):
    id: int

    class Config:
        orm_mode = True

# ---- GestaoDeEstudos ----
class GestaoDeEstudosBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    tipo_estudo: str
    status: Optional[Status] = None
    carga_horaria: Optional[int] = 0
    total_professores: int = 0
    total_alunos: int = 0

class GestaoDeEstudosCreate(GestaoDeEstudosBase):
    pass

class GestaoDeEstudosUpdate(GestaoDeEstudosBase):
    pass

class GestaoDeEstudosOut(GestaoDeEstudosBase):
    id: int

    class Config:
        orm_mode = True

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

class GestaoDeProfessoresCreate(GestaoDeProfessoresBase):
    pass

class GestaoDeProfessoresUpdate(GestaoDeProfessoresBase):
    pass

class GestaoDeProfessoresOut(GestaoDeProfessoresBase):
    id: int

    class Config:
        orm_mode = True

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

class GestaoDeAlunosCreate(GestaoDeAlunosBase):
    pass

class GestaoDeAlunosUpdate(GestaoDeAlunosBase):
    pass

class GestaoDeAlunosOut(GestaoDeAlunosBase):
    id: int

    class Config:
        orm_mode = True

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

    class Config:
        orm_mode = True

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

    class Config:
        orm_mode = True
