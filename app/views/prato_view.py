from fastapi import APIRouter, HTTPException
from typing import List
from app.models.prato import Prato, PratoRequest
from app.controller.prato_controller import PratoController

router = APIRouter(
    prefix="/prato",
    tags=["prato"],
)

@router.get("/", response_model=List[Prato])
async def read_pratos():
    PratoList = PratoController.getListaPratos() 
    return PratoList

@router.post("/", response_model=Prato)
async def criar_prato(prato: PratoRequest):
    novo_prato = PratoController.adicionarPrato(prato)
    return novo_prato

@router.put("/{idPrato}", response_model=Prato)
async def editar_prato(idPrato: int, novo_prato: PratoRequest):
    prato = PratoController.editarPrato(idPrato, novo_prato)
    if prato is None:
        raise HTTPException(status_code=404, detail="Prato não encontrado")
    return prato

@router.delete("/{idPrato}")
async def excluir_prato(idPrato: int):
    prato = PratoController.removePrato(idPrato)
    if prato is None:
        raise HTTPException(status_code=404, detail="Prato não encontrado")
    return prato

# @router.get("/informacaoNutricional/{idPrato}", response_model=str)
# async def read_info_prato(idPrato: int):
#     prato = PratoController.getPrato(idPrato)
#     if prato is None:
#         raise HTTPException(status_code=404, detail="Prato não encontrado")
#     return prato.getInformacaoNutricional()
