from fastapi import APIRouter, HTTPException
from typing import List
from app.models.refeicao import Refeicao
from app.controller.refeicao_controller import RefeicaoController
from typing import Literal

router = APIRouter(
    prefix="/refeicao",
    tags=["refeicao"],
)

@router.post("/", response_model=Refeicao)
async def adicionarRefeicao(horario: Literal["Café da manhã", "Almoço", "Janta"], idCardapio: int):
    nova_refeicao = RefeicaoController.adicionarRefeicao(horario, idCardapio)   
    if nova_refeicao is None:
        raise HTTPException(status_code=404, detail="Cardápio não encontrado")
    return nova_refeicao

@router.get("/{idRefeicao}", response_model=Refeicao)
async def selecionaRefeicao(idRefeicao: int):
    refeicao = RefeicaoController.getRefeicao(idRefeicao)
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

