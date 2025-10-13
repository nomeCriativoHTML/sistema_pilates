from sqlalchemy.orm import Session
from app.models.aluno import MinhaConta
from app.schema.aluno import MinhaContaCreate, MinhaContaUpdate
from fastapi import HTTPException

class AlunoController:
    
    @staticmethod
    def criar_aluno(db: Session, aluno: MinhaContaCreate):
        # Verificar se email já existe
        aluno_existente = db.query(MinhaConta).filter(MinhaConta.email == aluno.email).first()
        if aluno_existente:
            raise HTTPException(status_code=400, detail="Email já cadastrado")
        
        db_aluno = MinhaConta(
            nome=aluno.nome,
            email=aluno.email,
            telefone=aluno.telefone,
            status_pagamento=aluno.status_pagamento
        )
        db.add(db_aluno)
        db.commit()
        db.refresh(db_aluno)
        return db_aluno
    
    @staticmethod
    def listar_alunos(db: Session):
        return db.query(MinhaConta).all()
    
    @staticmethod
    def obter_aluno(db: Session, aluno_id: int):
        return db.query(MinhaConta).filter(MinhaConta.oid == aluno_id).first()
    
    @staticmethod
    def atualizar_aluno(db: Session, aluno_id: int, aluno_data: dict):
        # Remover campos None do update
        aluno_data = {k: v for k, v in aluno_data.items() if v is not None}
        
        if not aluno_data:
            raise HTTPException(status_code=400, detail="Nenhum dado para atualizar")
        
        db.query(MinhaConta).filter(MinhaConta.oid == aluno_id).update(aluno_data)
        db.commit()
        return db.query(MinhaConta).filter(MinhaConta.oid == aluno_id).first()
    
    @staticmethod
    def excluir_aluno(db: Session, aluno_id: int):
        aluno = db.query(MinhaConta).filter(MinhaConta.oid == aluno_id).first()
        if aluno:
            db.delete(aluno)
            db.commit()
        return aluno