# 🌱 API Tere Verde

Sistema de backend RESTful com autenticação JWT para a plataforma Tere Verde, voltado para gerenciamento de usuários administradores, autenticação segura e controle de recursos protegidos.

---

## ✅ Tecnologias Utilizadas

- **FastAPI** – Framework web moderno e rápido
- **SQLAlchemy** – ORM para banco de dados relacional
- **JWT (via jose)** – Autenticação baseada em token
- **passlib[bcrypt]** – Hash seguro de senhas
- **SQLite** (ou PostgreSQL, se configurado)
- **Uvicorn** – Servidor ASGI para execução

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/tere-verde-api.git
cd tere-verde-api

Crie e ative um ambiente virtual

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

Instale as dependências : pip install -r requirements.txt

Execute a aplicação: uvicorn app.main:app --reload



