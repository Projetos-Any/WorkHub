# Como contribuir

Este guia mostra o fluxo do time do começo ao fim. Se for sua primeira vez, siga na ordem. Na dúvida, pergunte no grupo: ninguém aqui nasceu sabendo.

> Regra de ouro: **ninguém faz commit direto na `main`**. Toda mudança entra por Pull Request (PR), com review de outra pessoa.

## 1. Pegue uma issue

1. Vá em **Issues** no GitHub e escolha uma tarefa que ninguém pegou ainda.
   Começando agora? Filtre pela etiqueta `good first issue`.
2. Na issue, clique em **Assignees → assign yourself** para avisar o time que você está nela.
3. Ficou com dúvida sobre a tarefa? Comente na própria issue antes de começar.

## 2. Atualize a main e crie sua branch

Sempre comece a partir da `main` atualizada:

```bash
git checkout main
git pull
```

Crie a branch com um nome curto que diga o que ela faz:

| Tipo de mudança | Padrão | Exemplo |
| --- | --- | --- |
| Funcionalidade nova | `feat/nome-curto` | `feat/cadastro-clientes` |
| Correção de bug | `fix/nome-curto` | `fix/total-orcamento` |
| Documentação | `docs/nome-curto` | `docs/readme-windows` |
| Configuração, ajustes gerais | `chore/nome-curto` | `chore/atualiza-dependencias` |

```bash
git checkout -b feat/cadastro-clientes
```

## 3. Faça commits pequenos

Usamos o padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/): `tipo: descrição em português, no presente`.

| Tipo | Quando usar |
| --- | --- |
| `feat` | funcionalidade nova |
| `fix` | correção de bug |
| `docs` | só documentação |
| `test` | só testes |
| `refactor` | mudança no código que não muda o comportamento |
| `style` | formatação, CSS |
| `chore` | configuração, dependências, coisas de manutenção |

```bash
git status                        # veja o que mudou
git add backend/app/routers/clientes.py
git commit -m "feat: adiciona rota de cadastro de clientes"
```

Dicas:

- Um commit = uma ideia. Prefira vários commits pequenos a um gigante.
- Evite `git add .` sem olhar o `git status` antes: é fácil mandar arquivo que não devia (como o `.env`).
- Antes de subir, rode o lint e os testes (veja no [README](README.md#rodando-lint-testes-e-build)).

## 4. Envie a branch e abra o Pull Request

```bash
git push -u origin feat/cadastro-clientes
```

O terminal mostra um link para abrir o PR. Também dá para ir no GitHub e clicar em **Compare & pull request**.

No PR:

1. A base deve ser a `main`.
2. Preencha o template que aparece (o que foi feito, como testar, checklist).
3. Escreva `Closes #12` (com o número da sua issue) para a issue fechar sozinha no merge.
4. Mudou alguma tela? Coloque um print, de preferência no tamanho de celular.

## 5. Peça review

1. No PR, em **Reviewers**, escolha pelo menos uma pessoa do time.
2. Espere o CI ficar verde (os checks aparecem no fim do PR). Se ficar vermelho, clique em **Details** para ver o erro.
3. Recebeu comentários? Corrija na mesma branch e suba de novo; o PR atualiza sozinho:

```bash
git add .
git commit -m "fix: ajusta validação apontada no review"
git push
```

A `main` andou enquanto você trabalhava e o GitHub avisa de conflito? Traga as novidades para sua branch:

```bash
git checkout main
git pull
git checkout feat/cadastro-clientes
git merge main
# resolva os conflitos no editor, depois:
git add .
git commit
git push
```

## 6. Merge só depois de aprovado

- O merge só acontece com **review aprovado e CI verde**.
- Depois do merge, apague a branch no GitHub (botão **Delete branch**) e atualize sua máquina:

```bash
git checkout main
git pull
git branch -d feat/cadastro-clientes
```

Pronto, pode pegar a próxima issue.

## Fazendo review de alguém

Revisar também é aprender. Ao revisar:

- Baixe a branch e teste: `git fetch` e depois `git checkout nome-da-branch`.
- Comente com gentileza e explique o porquê. Sugestões são bem-vindas, críticas sem explicação não.
- Aprovou? Clique em **Review changes → Approve**.

## Mudou o banco? Crie uma migration

Toda vez que criar ou alterar um model em `backend/app/models/`:

```bash
cd backend
alembic revision --autogenerate -m "cria tabela de clientes"
alembic upgrade head
```

Abra o arquivo gerado em `backend/alembic/versions/` e confira se faz o que você espera. Ele vai junto no seu PR.
Lembre de importar o model novo em `backend/app/models/__init__.py`, senão o Alembic não enxerga a tabela.

## Deu erro? Comece por aqui

### "port is already allocated" ou "address already in use"

Alguma coisa já está usando a porta (5432, 8000 ou 5173). Pode ser outro projeto, um Postgres instalado na máquina ou o próprio WorkHub rodando em outro terminal.

- Pare o que estiver rodando: `docker compose down` aqui e nos outros projetos, ou `Ctrl + C` nos terminais.
- Descubra quem está usando a porta: `lsof -i :8000` (Mac/Linux) ou `netstat -ano | findstr :8000` (Windows).
- Ou troque a porta no `.env` (`POSTGRES_PORT`, `API_PORT`, `WEB_PORT`). Se trocar a da API, ajuste o `VITE_API_URL` em `frontend/.env`; se trocar a do front, ajuste o `CORS_ORIGINS`.
- No modo desenvolvimento, passe a porta direto no comando: `uvicorn app.main:app --reload --port 8001` e `npm run dev -- --port 5174`.

### "Cannot connect to the Docker daemon" ou "docker: command not found"

O Docker Desktop está fechado. Abra o Docker Desktop, espere aparecer "Engine running" e rode o comando de novo.

### Mudei o `requirements.txt` ou o `package.json` e nada mudou

Faltou o `--build`. Sem ele, o Docker usa a imagem antiga, sem as dependências novas:

```bash
docker compose up --build
```

Ainda estranho? Recrie do zero (isso **não** apaga os dados do banco):

```bash
docker compose down
docker compose up --build --force-recreate --renew-anon-volumes
```

### Erro de CORS no console do navegador

Aparece algo como `blocked by CORS policy`. O navegador só deixa o front chamar a API se o endereço do front estiver liberado.

- Confira se você abriu o front pelo mesmo endereço que está no `CORS_ORIGINS` do `.env` (ex.: `http://localhost:5173`).
- Mudou o `.env`? Reinicie a API (`Ctrl + C` e suba de novo).
- Quer testar no celular, na mesma rede Wi-Fi? Abra `http://IP-DO-SEU-PC:5173`, coloque `VITE_API_URL=http://IP-DO-SEU-PC:8000` em `frontend/.env` e adicione `http://IP-DO-SEU-PC:5173` no `CORS_ORIGINS`.

### A página mostra "API: fora do ar"

- A API está rodando? Abra http://localhost:8000/health no navegador.
- Deu erro 503? A API não consegue falar com o banco: confira se o `db` está de pé (`docker compose ps`).

### "env file .env not found"

Você esqueceu de criar o `.env`: rode `cp .env.example .env` na raiz do projeto.

### Erro de senha do banco ("password authentication failed")

O Postgres só lê usuário e senha na primeira vez que cria o banco. Se você mudou o `.env` depois, apague o volume e suba de novo (isso **apaga os dados** do banco local):

```bash
docker compose down -v
docker compose up --build
```

### `ModuleNotFoundError` no modo desenvolvimento

A venv não está ativada. Rode `source .venv/bin/activate` dentro de `backend/` (Windows: `.venv\Scripts\activate`). O começo da linha do terminal deve mostrar `(.venv)`.
