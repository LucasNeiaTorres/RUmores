from fastapi import APIRouter, HTTPException
from typing import List
from app.models.cardapio import Cardapio
from app.controller.cardapio_controller import CardapioController
from datetime import date


router = APIRouter(
    prefix="/cardapio",
    tags=["cardapio"],
)

@router.get("/dia/{data}")
async def abrirCardapio(data: date):
    lista_pratos = CardapioController.abrirCardapioDia(data)
    if lista_pratos is None:
        raise HTTPException(status_code=404, detail="Cardápio não encontrado")
    return lista_pratos

@router.post("/", response_model=Cardapio)
async def adicionarCardapio(data: date):
    novo_cardapio = CardapioController.adicionarCardapio(data)
    return novo_cardapio

@router.get("/{idCardapio}", response_model=Cardapio)
async def selecionaCardapio(idCardapio: int):
    cardapio = CardapioController.getCardapio(idCardapio)
    if cardapio is None:
        raise HTTPException(status_code=404, detail="Cardapio não encontrado")
    return cardapio

# @router.put("/{i 

@router.delete("/{idCardapio}")
async def excluirCardapio(idCardapio: int):
    cardapio = CardapioController.removeCardapio(idCardapio)
    if cardapio is None:
        raise HTTPException(status_code=404, detail="Cardapio não encontrado")
    return cardapio

@router.get("/", response_model=List[Cardapio])
async def ObterListaCardapios():
    cardapioList = CardapioController.getListaCardapio() 
    return cardapioList