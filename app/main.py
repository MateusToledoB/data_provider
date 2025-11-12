from fastapi import FastAPI
from app.database import Base, engine
from app.routers import contacts

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Inicializa o app
app = FastAPI(
    title="API de Contatos",
    description="API para conumsulta de contatos por CPF com autenticação de usuário.",
    version="1.0.0"
)

# Inclui o router de contatos
app.include_router(contacts.router)

# Rota raiz só pra teste rápido
@app.get("/")
def root():
    return {"message": "API de contatos está rodando!"}
