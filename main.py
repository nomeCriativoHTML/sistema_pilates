#TESTE DE CONEXÃO COM O BANCO DE DADOS
from sqlalchemy import text
from app.database.connection import engine

try:
    # Conecta e testa
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("Conexão com MySQL funcionando!", result.fetchone())
except Exception as e:
    print("Erro ao conectar:", e)
