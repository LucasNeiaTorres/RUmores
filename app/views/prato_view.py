from fastapi import APIRouter, HTTPException
from typing import List
from app.models.prato import Prato, PratoRequest
from app.controller.prato_controller import PratoController
from app.controller.usuario_controller import UsuarioController

router = APIRouter(
    prefix="/prato",
    tags=["prato"],
)

@router.post("/", response_model=Prato)
async def adicionarPrato(prato: PratoRequest):
    if UsuarioController.getUsuarioLogado() is None or UsuarioController.getUsuarioLogado().getTipo() != "Nutricionista":
        raise HTTPException(status_code=401, detail="Nutricionista não logado")
    
    novo_prato = PratoController.adicionarPrato(prato)
    if novo_prato is None:
        raise HTTPException(status_code=401, detail="Prato já existente")
    return novo_prato

@router.get("/{idPrato}", response_model=Prato)
async def selecionaPrato(idPrato: int):
    prato = PratoController.selecionarPrato(idPrato)
    if prato is None:
        raise HTTPException(status_code=404, detail="Prato não encontrado")
    return prato

@router.put("/{idPrato}", response_model=Prato)
async def editarPrato(idPrato: int, novo_prato: PratoRequest):
    if UsuarioController.getUsuarioLogado() is None or UsuarioController.getUsuarioLogado().getTipo() != "Nutricionista":
        raise HTTPException(status_code=401, detail="Nutricionista não logado")
    prato = PratoController.editarPrato(idPrato, novo_prato)
    if prato is None:
        raise HTTPException(status_code=404, detail="Prato não encontrado")
    return prato

@router.delete("/{idPrato}")
async def excluirPrato(idPrato: int):
    if UsuarioController.getUsuarioLogado() is None or UsuarioController.getUsuarioLogado().getTipo() != "Nutricionista":
        raise HTTPException(status_code=401, detail="Nutricionista não logado")
    prato = PratoController.removePrato(idPrato)
    if prato is None:
        raise HTTPException(status_code=404, detail="Prato não encontrado")
    return prato

@router.get("/", response_model=List[Prato])
async def obterListaPratos():
    pratoList = PratoController.getListaPratos() 
    return pratoList

# @router.get("/informacaoNutricional/{idPrato}", response_model=str)
# async def read_info_prato(idPrato: int):
#     prato = PratoController.getPrato(idPrato)
#     if prato is None:
#         raise HTTPException(status_code=404, detail="Prato não encontrado")
#     return prato.getInformacaoNutricional()
