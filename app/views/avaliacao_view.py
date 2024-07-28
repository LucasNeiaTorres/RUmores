from fastapi import APIRouter, HTTPException
from typing import List
from app.models.avaliacao import Avaliacao, AvaliacaoRequest
from app.controller.avaliacao_controller import AvaliacaoController

router = APIRouter(
    prefix="/avaliacao",
    tags=["avaliacao"],
)

@router.post("/", response_model=Avaliacao)
async def adicionarAvaliacao(avaliacao: AvaliacaoRequest):
    nova_avaliacao = AvaliacaoController.adicionarAvaliacao(avaliacao)
    return nova_avaliacao   

@router.get("/{idAvaliacao}", response_model=Avaliacao)
async def selecionaAvaliacao(idAvaliacao: int):
    avaliacao = AvaliacaoController.getAvaliacao(idAvaliacao)
    if avaliacao is None:
        raise HTTPException(status_code=404, detail="Avaliacao não encontrada")
    return avaliacao

@router.put("/{idAvaliacao}", response_model=Avaliacao)
async def editarAvaliacao(idAvaliacao: int, nova_avaliacao: AvaliacaoRequest):
    avaliacao = AvaliacaoController.editarAvaliacao(idAvaliacao, nova_avaliacao)
    if avaliacao is None:
        raise HTTPException(status_code=404, detail="Avaliacao não encontrada")
    return avaliacao

@router.delete("/{idAvaliacao}")
async def excluirAvaliacao(idAvaliacao: int):
    avaliacao = AvaliacaoController.removeAvaliacao(idAvaliacao)
    if avaliacao is None:
        raise HTTPException(status_code=404, detail="Avaliacao não encontrada")
    return avaliacao

@router.get("/", response_model=List[Avaliacao])
async def ObterListaAvaliacoes():
    avaliacaoList = AvaliacaoController.getListaAvaliacoes() 
    return avaliacaoList