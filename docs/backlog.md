# Backlog inicial

Tarefas sugeridas para virarem issues, na ordem em que fazem sentido. As marcadas com `good first issue` são boas para começar.
Cada uma vira uma issue usando o template **Tarefa**. Nenhuma está implementada ainda.

| # | Tarefa | Etiquetas |
| --- | --- | --- |
| 1 | Model e migration do prestador | `backend` `good first issue` |
| 2 | Cadastro do prestador (API) | `backend` |
| 3 | Tela de cadastro do prestador | `frontend` `good first issue` |
| 4 | Login do prestador | `backend` `frontend` |
| 5 | Cadastro de clientes (API) | `backend` `good first issue` |
| 6 | Tela de clientes | `frontend` |
| 7 | Catálogo de serviços com preço (API) | `backend` `good first issue` |
| 8 | Tela do catálogo de serviços | `frontend` |
| 9 | Criação de orçamento com itens (API) | `backend` |
| 10 | Cálculo do total do orçamento | `backend` `good first issue` |
| 11 | Tela de criar orçamento no celular | `frontend` |
| 12 | Lista de orçamentos | `frontend` `good first issue` |
| 13 | Gerar PDF do orçamento | `backend` |
| 14 | Botão para enviar o orçamento pelo WhatsApp | `frontend` |

---

### 1. Model e migration do prestador

`backend` `good first issue`

Criar o model `Prestador` em `backend/app/models/` (nome, telefone, e-mail, profissão) e gerar a primeira migration de verdade com `alembic revision --autogenerate`. É a primeira tabela do projeto e serve de exemplo para as próximas.

### 2. Cadastro do prestador (API)

`backend`

Rota `POST /prestadores` para cadastrar e `GET /prestadores/{id}` para consultar. Criar os schemas em `app/schemas/`, o router em `app/routers/` e os testes em `tests/`.

### 3. Tela de cadastro do prestador

`frontend` `good first issue`

Página com formulário (nome, telefone, e-mail, profissão) que chama a API pelo `services/api.js`. Campos grandes, fáceis de tocar no celular.

### 4. Login do prestador

`backend` `frontend`

Adicionar senha ao prestador (guardada com hash, nunca em texto puro), rota de login que devolve um token e tela de login. Depois disso, as rotas passam a saber qual prestador está logado.

### 5. Cadastro de clientes (API)

`backend` `good first issue`

Model, migration e rotas para criar, listar, editar e apagar clientes (nome, telefone, endereço). Cada cliente pertence a um prestador.

### 6. Tela de clientes

`frontend`

Lista de clientes com busca pelo nome e formulário para cadastrar um novo. Pensada para o celular: um cliente por linha, botão de "novo cliente" sempre à mão.

### 7. Catálogo de serviços com preço (API)

`backend` `good first issue`

Model, migration e rotas para os serviços que o prestador oferece (ex.: "Instalação de tomada", R$ 80,00). Atenção: dinheiro deve usar `Numeric`/`Decimal`, nunca `float`.

### 8. Tela do catálogo de serviços

`frontend`

Listar, criar e editar os serviços com seus preços. O preço aparece formatado em reais (`R$ 80,00`).

### 9. Criação de orçamento com itens (API)

`backend`

Model, migration e rotas do orçamento: pertence a um cliente e tem vários itens (serviço, quantidade, preço unitário). O preço é copiado do catálogo na hora, para o orçamento antigo não mudar se o preço do catálogo mudar.

### 10. Cálculo do total do orçamento

`backend` `good first issue`

Função em `app/services/` que calcula o subtotal de cada item e o total do orçamento (com desconto opcional). Bem coberta por testes com pytest.

### 11. Tela de criar orçamento no celular

`frontend`

A tela principal do app: escolher o cliente, adicionar serviços do catálogo, ajustar quantidades e ver o total atualizando na hora. Meta: montar um orçamento em menos de 1 minuto.

### 12. Lista de orçamentos

`frontend` `good first issue`

Tela com os orçamentos já feitos (cliente, data, total), do mais recente para o mais antigo, com acesso aos detalhes de cada um.

### 13. Gerar PDF do orçamento

`backend`

Rota que devolve o orçamento em PDF com os dados do prestador, do cliente, os itens e o total. Antes de começar, comparar bibliotecas e combinar com o time qual usar.

### 14. Botão para enviar o orçamento pelo WhatsApp

`frontend`

Botão na tela do orçamento que abre o WhatsApp com uma mensagem pronta para o cliente (link `https://wa.me/`), com o resumo e o link do PDF.
