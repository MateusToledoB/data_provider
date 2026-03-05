# Data Provider API

Uma API RESTful para consulta de contatos com autenticação segura de usuários.

## 📋 Sobre

API desenvolvida em FastAPI que fornece endpoints autenticados para busca de informações de contatos por CPF, com validação robusta de dados e gerenciamento seguro de credenciais.

## 🛠️ Tecnologias

| Tecnologia | Versão | Função |
|------------|--------|--------|
| **FastAPI** | 0.121.1 | Framework web assíncrono |
| **SQLAlchemy** | 2.0.44 | ORM para persistência de dados |
| **PyMySQL** | 1.1.2 | Driver MySQL |
| **Pydantic** | 2.12.4 | Validação de esquemas |
| **Passlib + Bcrypt** | 1.7.4 + 4.1.2 | Autenticação e hash de senhas |
| **Uvicorn** | 0.38.0 | Servidor ASGI |
| **python-dotenv** | 1.2.1 | Gestão de variáveis de ambiente |

## 🏗️ Arquitetura

```
app/
├── main.py           # Inicialização e configuração da aplicação
├── database.py       # Conexão e sessão do banco de dados
├── models.py         # Definição das entidades (User, Numero)
├── schemas.py        # Esquemas de validação (Pydantic)
└── routers/
    └── contacts.py   # Endpoints de contatos
```

### Camadas

- **Routers:** Endpoints HTTP e lógica de autenticação
- **Schemas:** Validação de entrada/saída via Pydantic
- **Models:** Mapeamento objeto-relacional com SQLAlchemy
- **Database:** Gerenciamento de conexões e sessões

## 🚀 Quick Start

### Pré-requisitos
- Python 3.8+
- MySQL

### Instalação

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Configuração

Crie um arquivo `.env` na raiz do projeto com as variáveis necessárias.

### Execução

```bash
python -m uvicorn app.main:app --reload
```

A API estará disponível em `http://localhost:8000`

## 📚 Documentação

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`
