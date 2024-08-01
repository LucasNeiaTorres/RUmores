from fastapi import APIRouter, HTTPException
from app.controller.cardapio_controller import CardapioController
from app.models.prato import Prato


from app.controller.refeicao_controller import RefeicaoController
from app.controller.refeicaoPrato_controller import RefeicaoPratoController
from app.views.prato_view import selecionaPrato as sp
# from app.views.abrir_cardapio_view import abrirCardapio

from datetime import date


router = APIRouter(
    prefix="/AcessarInfoNutricionais",
    tags=["Acessar Informações Nutricionais"],
)

@router.get("/cardapio/{data}")
async def abrirCardapio(data: date):
    lista_pratos = CardapioController.abrirCardapioDia(data)
    if lista_pratos is None:
        raise HTTPException(status_code=404, detail="Cardápio não encontrado")
    return lista_pratos

@router.get("/prato/{idPrato}", response_model=Prato)
async def selecionaPrato(idPrato: int):
    prato = await sp(idPrato)
    if prato is None:
        raise HTTPException(status_code=404, detail="Prato não encontrado")
    return prato


# TODO: 
# - tira algumas rotas de estudante e nutricionista e coloca aqui