# RUmores

API REST para **avaliação do Restaurante Universitário (RU)**: a nutricionista
publica o cardápio do dia e as informações nutricionais dos pratos, e o estudante
autenticado dá nota de 1 a 5 com comentário. Feita em **FastAPI**, com a
documentação interativa gerada automaticamente em `/docs`.

O nome é um trocadilho: **RU** (o restaurante) + **rumores**, o burburinho de
quem reclama ou elogia a comida.

## Contexto

Trabalho acadêmico, feito **em dupla**. O foco era praticar modelagem
orientada a objetos e uma API em camadas — por isso o código separa
`models`, `controller` e `view` mesmo sendo um protótipo pequeno, e há um
diagrama de classes versionado em `diragramaClasses.png`.

## O que dá para fazer

Dois papéis, com permissões distintas:

- **Nutricionista** — adiciona informações nutricionais dos pratos e monta o
  cardápio do dia.
- **Estudante** — consulta os pratos, lê as informações nutricionais e registra
  uma avaliação (nota de 1 a 5 + comentário) do prato que comeu.

Cada caso de uso é um roteador próprio, montado em `main.py`:
`RegistrarReviewPrato`, `AcessarInformacoesNutricionais`,
`AdicionarInformacoesNutricionais`, `AdicionarCardapioDoDia`.

## A decisão que marca o projeto: sem banco, tudo em memória

Não há banco de dados. As listas de usuários, pratos, cardápios e avaliações
são **atributos de classe** nos controllers (`UsuarioController.listaUsuarios`,
`AvaliacaoController.listaAvaliacoes`, …), semeadas com dados de exemplo. O
`app/database.py` chegou a ser esboçado com SQLAlchemy + SQLite, mas está
**inteiramente comentado** — a persistência ficou como próximo passo, não como
entrega.

Isso mantém o protótipo rodável com `uvicorn` e nada mais, ao custo de os dados
se perderem a cada reinício. É uma escolha consciente de escopo, não um
esquecimento.

## Como rodar

```sh
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

A raiz (`/`) redireciona para a documentação interativa:
**http://localhost:8000/docs** — de onde dá para exercitar todos os endpoints.

## Limitações conhecidas (é protótipo)

- **Sem persistência** — dados em memória, some ao reiniciar (ver acima).
- **Sessão global** — o "usuário logado" é uma única variável de classe
  (`usuario_logado`), então o servidor atende um usuário por vez; não é login
  multiusuário de verdade.
- **Senha em texto puro** — o login compara a senha diretamente, sem hash. Serve
  para demonstrar o fluxo, não para produção.
- **CORS aberto** (`allow_origins=['*']`) — conveniente para desenvolvimento,
  inseguro fora dele.

## Estrutura

```
main.py                  monta a aplicação e os roteadores; redireciona / -> /docs
requirements.txt         fastapi, uvicorn
diragramaClasses.png     diagrama de classes do modelo
app/
  models/                Pydantic: usuario (Estudante/Nutricionista), prato,
                         avaliacao, cardapio, refeicao
  controller/            regras + "repositório" em memória de cada entidade
  views/                 um roteador FastAPI por caso de uso
  database.py            esboço de persistência (comentado, não usado)
```
