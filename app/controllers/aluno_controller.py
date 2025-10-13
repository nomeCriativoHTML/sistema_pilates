from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.aluno import Aluno
from app.schema.aluno import AlunoCreate, AlunoUpdate

class AlunoController:

    @staticmethod
    def criar_aluno(db: Session, aluno: AlunoCreate):
        # Verificar se o email já existe
        aluno_existente = db.query(Aluno).filter(Aluno.email == aluno.email).first()
        if aluno_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="E-mail já cadastrado."
            )

        # Criar novo aluno
        novo_aluno = Aluno(
            nome=aluno.nome,
            telefone=aluno.telefone,
            email=aluno.email,
            data_nascimento=aluno.data_nascimento,
            status_pagamento=aluno.status_pagamento
        )

        db.add(novo_aluno)
        db.commit()
        db.refresh(novo_aluno)
        return novo_aluno

    @staticmethod
    def listar_alunos(db: Session):
        alunos = db.query(Aluno).all()
        return alunos

    @staticmethod
    def obter_aluno(db: Session, aluno_id: int):
        aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
        if not aluno:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Aluno não encontrado."
            )
        return aluno

    @staticmethod
    def atualizar_aluno(db: Session, aluno_id: int, aluno_data: AlunoUpdate):
        aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
        if not aluno:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Aluno não encontrado."
            )

        update_data = aluno_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(aluno, key, value)

        db.commit()
        db.refresh(aluno)
        return aluno

    @staticmethod
    def excluir_aluno(db: Session, aluno_id: int):
        aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
        if not aluno:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Aluno não encontrado."
            )

        db.delete(aluno)
        db.commit()
        return {"mensagem": f"Aluno {aluno.nome} excluído com sucesso."}
