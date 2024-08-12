# main.py
from fastapi import FastAPI
from app.views import registrar_review_de_prato_view, acessar_informacoes_nutricionais_view, adicionar_informacoes_nutricionais_view, adicionar_cardapio_do_dia_view, utils_view
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API do Sistema de Avaliação do RU",
    description="",
    version="0.0.1",
)

app.include_router(acessar_informacoes_nutricionais_view.router)
app.include_router(adicionar_informacoes_nutricionais_view.router)
app.include_router(registrar_review_de_prato_view.router)
app.include_router(adicionar_cardapio_do_dia_view.router)
app.include_router(utils_view.router)


# TODO: 
# - usar set e get principalmente nos editar
# - tirar logica das views
# - não chamar outras views

# Perguntas:
#     - Coloca as classes de Request para o diagrama de classes
#     - BD

# CORS
origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# redireciona '/' para '/docs'
@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url="/docs")
