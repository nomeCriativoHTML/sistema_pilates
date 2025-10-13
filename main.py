from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app = FastAPI()

# Configuração de templates e arquivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir todas as rotas
try:
    from app.routes.aluno_routes import router as aluno_router
    app.include_router(aluno_router, prefix="/alunos", tags=["Alunos"])
    print("✅ Rotas de alunos carregadas com sucesso!")
except Exception as e:
    print(f"⚠️  Erro ao carregar rotas de alunos: {e}")

try:
    from app.routes.admin_routes import router as admin_router
    app.include_router(admin_router, prefix="/admin", tags=["Admin"])
    print("✅ Rotas de admin carregadas com sucesso!")
except Exception as e:
    print(f"❌ Erro ao carregar rotas de admin: {e}")

try:
    from app.routes.login_routes import router as login_router
    app.include_router(login_router, tags=["Login"])
    print("✅ Rotas de login carregadas com sucesso!")
except ImportError:
    print("ℹ️  Rotas de login não encontradas")

# Rota principal redireciona para o cadastro
@app.get("/")
async def root():
    return RedirectResponse(url="/alunos/cadastro")

# Rota para página inicial/dashboard
@app.get("/home")
async def home(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)