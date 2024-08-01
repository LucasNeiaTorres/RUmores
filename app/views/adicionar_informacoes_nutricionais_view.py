from fastapi import APIRouter, HTTPException
from app.models.prato import Prato, PratoRequest
from app.models.usuario import Nutricionista, LoginRequest
from typing import List
from app.views.prato_view import selecionaPrato as sp, adicionarPrato as ap, obterListaPratos, editarPrato as ep
from app.views.usuario_view import inserirLogin
from app.controller.usuario_controller import UsuarioController

router = APIRouter(
    prefix="/AdicionarInfoNutricionais",
    tags=["Adicionar Informações Nutricionais"],
)

@router.post("/login_nutricionista", response_model=Nutricionista)
async def loginNutricionista(nutricionista: LoginRequest):
    user = await inserirLogin(nutricionista)
    if user is None or user.getTipo() != "Nutricionista":
        raise HTTPException(status_code=404, detail="Nutricionista não encontrado")
    return user

@router.get("/pratos/", response_model=List[Prato])
async def gerenciamentoPratos():
    if UsuarioController.getUsuarioLogado() is None or UsuarioController.getUsuarioLogado().getTipo() != "Nutricionista":
        raise HTTPException(status_code=401, detail="Nutricionista não logado")
    
    pratos = await obterListaPratos()
    if pratos is None:
        raise HTTPException(status_code=404, detail="Pratos não encontrados")
    return pratos

@router.post("/prato/", response_model=Prato)
async def adicionarPrato(prato: PratoRequest):
    prato = await ap(prato)
    return prato

@router.put("/prato/{idPrato}", response_model=Prato)
async def editarPrato(idPrato: int, novo_prato: PratoRequest):
    prato = await ep(idPrato, novo_prato)
    if prato is None:
        raise HTTPException(status_code=404, detail="Prato não encontrado")
    return prato