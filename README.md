# 🌱 API Tere Verde

Sistema de backend desenvolvido com FastAPI para gerenciamento de trilhas, parques, biodiversidade e ações ambientais na cidade de Teresópolis. Projeto acadêmico do curso de Análise e Desenvolvimento de Sistemas – UNIFESO.

---

## 📌 Índice

- [📖 Sobre o Projeto](#📖-sobre-o-projeto)
- [🚀 Tecnologias Utilizadas](#🚀-tecnologias-utilizadas)
- [🧱 Arquitetura](#🧱-arquitetura)
- [🔐 Autenticação](#🔐-autenticação)
- [📦 Instalação e Execução](#📦-instalação-e-execução)
- [📬 Rotas da API](#📬-rotas-da-api)
- [🛠️ Próximos Passos](#🛠️-próximos-passos)
- [📄 Licença](#📄-licença)

---

## 📖 Sobre o Projeto

A **API Tere Verde** tem como objetivo principal promover o controle e gestão de dados ambientais de forma eficiente e segura. A aplicação centraliza o cadastro e controle de:

- Administradores (com login seguro via token JWT)
- Trilhas e parques
- Biodiversidade local (ex: animais catalogados)
- Eventos ambientais e ações sustentáveis

Este projeto visa apoiar ações reais ou simuladas de preservação, turismo ecológico e coleta seletiva.

---

## 🚀 Tecnologias Utilizadas

- 💡 **[FastAPI]** – Framework Web moderno em Python
- 🐘 **SQLite** 
- 🧠 **SQLAlchemy** – ORM para manipulação de dados
- 🛡️ **JWT Auth** – Segurança com tokens
- 🧪 **Swagger** – Documentação interativa automática
- 📬 **Postman** – Testes de integração da API

---

## 🧱 Arquitetura

A organização do projeto segue uma estrutura modular, separando responsabilidades de forma clara para facilitar a manutenção, escalabilidade e testes. Abaixo, uma visão geral dos diretórios e arquivos principais:

📦 app/
├── 📁 auth/           # Lógica de autenticação (JWT, verificação de senha, login)
│   └── auth.py
│

├── 📁 models/         # Contém os modelos do banco de dados (SQLAlchemy)
│   └── administrador.py
│

├── 📁 routers/        # Define as rotas da aplicação (FastAPI Routers)
│   └── login.py
│   └── administrador.py
│

├── 📁 schemas/        # Esquemas Pydantic usados para validação e contratos de entrada/saída
│   └── administrador.py
│

├── 📁 services/       # Lógica adicional de negócio.
│   └── parque.py
│


├── __init__.py        # Torna a pasta um pacote Python
├── create_db.py       # Script opcional para criação do banco (caso necessário)
├── database.py        # Conexão com o banco de dados (Session e engine)
├── main.py            # Arquivo principal da aplicação FastAPI
├── seed.py            # Script para popular o banco com dados iniciais




## 🚀 Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Michaelreisrodrigues/mvp-back-end.git
cd tere-verde-api

Crie e ative um ambiente virtual

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


Instale as dependências : pip install -r requirements.txt

Execute a aplicação: uvicorn app.main:app --reload

Acesse a documentação interativa da API:
 http://localhost:8000/docs



