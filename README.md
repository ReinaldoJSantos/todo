# 📝 Todo API — FastAPI

API REST para gerenciamento de tarefas, com autenticação JWT e estrutura profissional.

## 🚀 Tecnologias

- Python 3.10
- FastAPI
- SQLAlchemy
- SQLite
- JWT
- Docker
- Docker Compose

## 📂 Estrutura do Projeto

app/
├── core/
│ ├── config.py
│ └── security.py
├── database/
│ ├── session.py
│ └── deps.py
├── models/
├── routes/
├── schemas/
└── main.py


## ⚙️ Configuração

Crie um arquivo `.env` na raiz:

```env
APP_NAME=Todo API
SECRET_KEY=dev-secret-key
DATABASE_URL=sqlite:///./todo.db
ACCESS_TOKEN_EXPIRE_MINUTES=30

▶️ Como rodar com Docker
docker compose up --build


Acesse:

http://localhost:8000/docs

🔐 Autenticação

Cadastro de usuário

Login com JWT

Rotas protegidas com Bearer Token

📌 Funcionalidades

CRUD de usuários

Login

CRUD de tarefas

Autorização por token

🧠 Decisões Técnicas

FastAPI pela performance e tipagem

SQLAlchemy como ORM

JWT para autenticação stateless

Docker para padronizar ambiente

Variáveis de ambiente para segurança

📈 Próximas melhorias

Banco PostgreSQL

Refresh Token

Testes automatizados

CI/CD
