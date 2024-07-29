from fastapi import APIRouter, HTTPException
from typing import List
from app.models.refeicaoPrato import RefeicaoPrato, RefeicaoPratoRequest
from app.controller.refeicaoPrato_controller import RefeicaoPratoController

router = APIRouter(
    prefix="/refeicaoPrato",
    tags=["refeicaoPrato"],
)

#TODO: Precisa?

@router.post("/", response_model=RefeicaoPrato)
async def adicionarRefeicaoPrato(refeicaoPrato: RefeicaoPratoRequest):
    novo_refeicaoPrato = RefeicaoPratoController.adicionarRefeicaoPrato(refeicaoPrato)
    return novo_refeicaoPrato

@router.get("/{idRefeicaoPrato}", response_model=RefeicaoPrato)
async def selecionaRefeicaoPrato(idRefeicaoPrato: int):
    refeicaoPrato = RefeicaoPratoController.getRefeicaoPrato(idRefeicaoPrato)
    if refeicaoPrato is None:
        raise HTTPException(status_code=404, detail="Refeição Prato não encontrado")
    return refeicaoPrato

@router.put("/{idRefeicaoPrato}", response_model=RefeicaoPrato)
async def editarRefeicaoPrato(idRefeicaoPrato: int, novo_refeicaoPrato: RefeicaoPratoRequest):
    refeicaoPrato = RefeicaoPratoController.editarRefeicaoPrato(idRefeicaoPrato, novo_refeicaoPrato)
    if refeicaoPrato is None:
        raise HTTPException(status_code=404, detail="Refeição Prato não encontrado")
    return refeicaoPrato

@router.delete("/{idRefeicaoPrato}")
async def excluirRefeicaoPrato(idRefeicaoPrato: int):
    refeicaoPrato = RefeicaoPratoController.removeRefeicaoPrato(idRefeicaoPrato)
    if refeicaoPrato is None:
        raise HTTPException(status_code=404, detail="Refeição Prato não encontrado")
    return refeicaoPrato 

@router.get("/", response_model=List[RefeicaoPrato])
async def ObterListaRefeicaoPrato():
    refeicaoPratoList = RefeicaoPratoController.getListaRefeicaoPrato()
    return refeicaoPratoList