# WorkHub

App para prestadores de serviço (eletricistas, marceneiros, técnicos de ar-condicionado) gerarem e enviarem orçamentos profissionais para o cliente em menos de 1 minuto, direto do celular.
Projeto colaborativo de um grupo de devs aprendendo juntos: a ideia é construir de verdade e aprender no caminho.

## Stack

| Parte | Tecnologias |
| --- | --- |
| Backend | Python 3.12, FastAPI, Uvicorn, SQLAlchemy 2, Alembic, Pydantic Settings |
| Frontend | React + Vite (JavaScript), React Router |
| Banco | PostgreSQL 16 |
| Infra | Docker e Docker Compose |
| Qualidade | Ruff e pytest (backend), ESLint (frontend), GitHub Actions (CI) |

## Pré-requisitos

- [Git](https://git-scm.com/downloads)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (já vem com o Docker Compose)
- [Python 3.12](https://www.python.org/downloads/) (só para o modo desenvolvimento)
- [Node.js](https://nodejs.org/) 22 ou mais novo, com npm (só para o modo desenvolvimento)

## Primeiro passo (para os dois jeitos)

```bash
git clone git@github.com:Projetos-Any/WorkHub.git
cd WorkHub
cp .env.example .env
```

O `.env` guarda as configurações locais (usuário e senha do banco, portas). Ele não vai para o Git.

## Jeito 1: rodar tudo com Docker

O jeito mais fácil: um comando sobe o banco, a API e o front.

```bash
docker compose up --build
```

Quando terminar de subir, abra:

| O quê | Endereço |
| --- | --- |
| App (front) | http://localhost:5173 |
| API | http://localhost:8000/health |
| Documentação da API | http://localhost:8000/docs |

A página inicial deve mostrar **API: ok**.

Para parar: `Ctrl + C` no terminal, ou `docker compose down` em outro terminal.
O código fica espelhado dentro dos containers, então é só salvar o arquivo que a API e o front recarregam sozinhos. Use `--build` de novo quando mudar o `requirements.txt` ou o `package.json`.

Alguma porta já está em uso por outro projeto? Troque `POSTGRES_PORT`, `API_PORT` ou `WEB_PORT` no `.env` (os comentários do `.env.example` explicam o que ajustar junto).

## Jeito 2: modo desenvolvimento

Só o banco roda no Docker; a API e o front rodam direto na sua máquina. É melhor para usar o debugger e ver os erros mais rápido. Use três terminais:

**Terminal 1: banco**

```bash
docker compose up db
```

**Terminal 2: API**

```bash
cd backend
python3.12 -m venv .venv         # Windows: py -3.12 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head             # aplica as migrations no banco
uvicorn app.main:app --reload
```

Da próxima vez, basta `cd backend`, `source .venv/bin/activate` e `uvicorn app.main:app --reload`.

**Terminal 3: front**

```bash
cd frontend
cp .env.example .env             # só na primeira vez
npm install
npm run dev
```

Os endereços são os mesmos da tabela acima. Não rode o Jeito 1 e o Jeito 2 ao mesmo tempo: os dois usam as mesmas portas.

### Rodando lint, testes e build

Os mesmos comandos que o CI roda em todo Pull Request:

```bash
# backend (com a venv ativada e o banco rodando)
cd backend
ruff check .          # procura problemas no código
ruff format .         # arruma a formatação
pytest                # roda os testes

# frontend
cd frontend
npm run lint
npm run build
```

## Estrutura de pastas

```
WorkHub/
├── docker-compose.yml       # sobe db, api e web juntos
├── .env.example             # modelo do .env (copie para .env)
├── CONTRIBUTING.md          # como o time trabalha (leia antes de começar!)
├── .github/                 # templates de issue e PR, e o CI (workflows/ci.yml)
├── docs/backlog.md          # tarefas iniciais sugeridas
├── backend/
│   ├── requirements.txt     # dependências do Python
│   ├── pyproject.toml       # configuração do Ruff e do pytest
│   ├── alembic/versions/    # migrations: o histórico de mudanças do banco
│   ├── app/
│   │   ├── main.py          # cria o app FastAPI, configura CORS e inclui as rotas
│   │   ├── config.py        # lê as variáveis de ambiente (.env)
│   │   ├── database.py      # conexão com o banco e sessão do SQLAlchemy
│   │   ├── routers/         # rotas da API (endpoints), um arquivo por assunto
│   │   ├── models/          # tabelas do banco (SQLAlchemy)
│   │   ├── schemas/         # formato dos dados que entram e saem (Pydantic)
│   │   └── services/        # regras de negócio
│   └── tests/               # testes automatizados (pytest)
└── frontend/
    ├── .env.example         # endereço da API (VITE_API_URL)
    ├── index.html           # página base onde o React é montado
    └── src/
        ├── main.jsx         # ponto de entrada do React
        ├── App.jsx          # lista das rotas (páginas) do app
        ├── services/api.js  # todas as chamadas para a API passam por aqui
        ├── pages/           # uma tela por arquivo
        ├── components/      # pedaços de tela reaproveitáveis
        └── styles/          # CSS global, mobile first, com as cores do app
```

## Quer contribuir?

Leia o [CONTRIBUTING.md](CONTRIBUTING.md): lá está o passo a passo de como pegar uma tarefa, criar sua branch e abrir um Pull Request, e também a seção **"Deu erro? Comece por aqui"**.
As tarefas iniciais sugeridas estão em [docs/backlog.md](docs/backlog.md).
