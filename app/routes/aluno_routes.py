from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.models.aluno import MinhaConta
from app.schema.aluno import MinhaContaCreate, MinhaContaUpdate
from app.controllers.aluno_controller import AlunoController
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

router = APIRouter()

# Página de cadastro
@router.get("/cadastro", response_class=HTMLResponse)
async def pagina_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

# Criar aluno via formulário web
@router.post("/cadastro/aluno")
async def criar_aluno(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    estudio: str = Form(None),
    status: str = Form(None),
    db: Session = Depends(get_db)
):
    try:
        aluno_data = MinhaContaCreate(
            nome=nome,
            email=email,
            telefone=telefone,
            status_pagamento=status
        )
        
        aluno = AlunoController.criar_aluno(db, aluno_data)
        # Redireciona de volta para o cadastro com mensagem de sucesso
        return RedirectResponse(url="/alunos/cadastro?success=true", status_code=303)
    
    except Exception as e:
        # Redireciona de volta com mensagem de erro
        return RedirectResponse(url=f"/alunos/cadastro?error={str(e)}", status_code=303)


# ===== API ENDPOINTS (CRUD COMPLETO) =====

# Listar todos os alunos (API)
@router.get("/")
def listar_alunos(db: Session = Depends(get_db)):
    return AlunoController.listar_alunos(db)

# Obter aluno específico (API)
@router.get("/{aluno_id}")
def obter_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = AlunoController.obter_aluno(db, aluno_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

# Atualizar aluno (API)
@router.put("/{aluno_id}")
def atualizar_aluno(
    aluno_id: int, 
    aluno_data: MinhaContaUpdate, 
    db: Session = Depends(get_db)
):
    aluno = AlunoController.atualizar_aluno(db, aluno_id, aluno_data.dict())
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

# Excluir aluno (API)
@router.delete("/{aluno_id}")
def excluir_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = AlunoController.excluir_aluno(db, aluno_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return {"message": "Aluno excluído com sucesso"}