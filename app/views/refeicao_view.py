from fastapi import APIRouter, HTTPException
from typing import List
from app.models.refeicao import Refeicao, RefeicaoRequest
from app.controller.refeicao_controller import RefeicaoController

router = APIRouter(
    prefix="/refeicao",
    tags=["refeicao"],
)

@router.post("/", response_model=Refeicao)
async def adicionarRefeicao(refeicao: RefeicaoRequest):
    nova_refeicao = RefeicaoController.adicionarRefeicao(refeicao)
    return nova_refeicao

@router.get("/{idRefeicao}", response_model=Refeicao)
async def selecionaRefeicao(idRefeicao: int):
    refeicao = RefeicaoController.getRefeicao(idRefeicao)
    if refeicao is None:
        raise HTTPException(status_code=404, detail="Refeição não encontrada")
    return refeicao

@router.put("/{idRefeicao}", response_model=Refeicao)
async def editarRefeicao(idRefeicao: int, nova_refeicao: RefeicaoRequest):
    refeicao = RefeicaoController.editarRefeicao(idRefeicao, nova_refeicao)
    if refeicao is None:
        raise HTTPException(status_code=404, detail="Refeição não encontrada")
    return refeicao

@router.delete("/{idRefeicao}")
async def excluirRefeicao(idRefeicao: int):
    refeicao = RefeicaoController.removeRefeicao(idRefeicao)
    if refeicao is None:
        raise HTTPException(status_code=404, detail="Refeição não encontrada")
    return refeicao

@router.get("/", response_model=List[Refeicao])
async def ObterListaRefeicoes():
    refeicaoList = RefeicaoController.getListaRefeicao() 
    return refeicaoList

