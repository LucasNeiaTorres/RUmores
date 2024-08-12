from fastapi import APIRouter, HTTPException
from app.controller.cardapio_controller import CardapioController
from app.models.prato import Prato
from app.models.cardapio import Cardapio
from app.controller.prato_controller import PratoController
from datetime import date
from typing import List


router = APIRouter(
    prefix="/AcessarInfoNutricionais",
    tags=["Acessar Informações Nutricionais"],
)

@router.get("/calendario/", response_model=List[Cardapio])
async def calendario():
    cardapioList = CardapioController.getListaCardapio() 
    return cardapioList

@router.get("/cardapio/{data}")
async def abrirCardapio(data: date):
    lista_pratos = CardapioController.abrirCardapioDia(data)
    if lista_pratos is None:
        raise HTTPException(status_code=404, detail="Cardápio não encontrado")
    return lista_pratos

@router.get("/prato/{idPrato}", response_model=Prato)
async def selecionaPrato(idPrato: int):
    prato = PratoController.selecionarPrato(idPrato)
    if prato is None:
        raise HTTPException(status_code=404, detail="Prato não encontrado")
    return prato
