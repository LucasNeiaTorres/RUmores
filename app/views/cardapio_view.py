from fastapi import APIRouter, HTTPException
from typing import List
from app.models.cardapio import Cardapio, CardapioRequest
from app.controller.cardapio_controller import CardapioController

router = APIRouter(
    prefix="/cardapio",
    tags=["cardapio"],
)

@router.post("/", response_model=Cardapio)
async def adicionarCardapio(cardapio: CardapioRequest):
    novo_cardapio = CardapioController.adicionarCardapio(cardapio)
    return novo_cardapio

@router.get("/{idCardapio}", response_model=Cardapio)
async def selecionaCardapio(idCardapio: int):
    cardapio = CardapioController.getCardapio(idCardapio)
    if cardapio is None:
        raise HTTPException(status_code=404, detail="Cardapio não encontrado")
    return cardapio

@router.put("/{idCardapio}", response_model=Cardapio)
async def editarCardapio(idCardapio: int, novo_cardapio: CardapioRequest):
    cardapio = CardapioController.editarCardapio(idCardapio, novo_cardapio)
    if cardapio is None:
        raise HTTPException(status_code=404, detail="Cardapio não encontrado")
    return cardapio

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