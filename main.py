# main.py
from fastapi import FastAPI
from app.views import prato_view, estudante_view, nutricionista_view, cardapio_view
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API do Sistema de Avaliação do RU",
    description="",
    version="0.0.1",
)

app.include_router(prato_view.router)
app.include_router(estudante_view.router)
app.include_router(nutricionista_view.router)
app.include_router(cardapio_view.router)

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
