from fastapi import APIRouter, HTTPException
from app.models.prato import Prato, PratoRequest
from app.models.usuario import Nutricionista
from typing import List
from app.controller.usuario_controller import UsuarioController
from app.controller.prato_controller import PratoController

router = APIRouter(
    prefix="/AdicionarInfoNutricionais",
    tags=["Adicionar Informações Nutricionais"],
)

@router.post("/login_nutricionista", response_model=Nutricionista)
async def loginNutricionista(email: str, senha: str):
    user = UsuarioController.login(email, senha)
    if user is None or user.getTipo() != "Nutricionista":
        raise HTTPException(status_code=404, detail="Nutricionista não encontrado")
    return user

@router.get("/pratos/", response_model=List[Prato])
async def gerenciamentoPratos():
    if UsuarioController.getUsuarioLogado() is None or UsuarioController.getUsuarioLogado().getTipo() != "Nutricionista":
        raise HTTPException(status_code=401, detail="Nutricionista não logado")
    
    pratos = PratoController.getListaPratos() 
    if pratos is None:
        raise HTTPException(status_code=404, detail="Pratos não encontrados")
    return pratos

@router.post("/prato/", response_model=Prato)
async def adicionarPrato(prato: PratoRequest):
    if UsuarioController.getUsuarioLogado() is None or UsuarioController.getUsuarioLogado().getTipo() != "Nutricionista":
        raise HTTPException(status_code=401, detail="Nutricionista não logado")

    novo_prato = PratoController.adicionarPrato(prato)
    if novo_prato is None:
        raise HTTPException(status_code=401, detail="Prato já existente")
    return novo_prato

@router.put("/prato/{idPrato}", response_model=Prato)
async def editarPrato(idPrato: int, novo_prato: PratoRequest):
    if UsuarioController.getUsuarioLogado() is None or UsuarioController.getUsuarioLogado().getTipo() != "Nutricionista":
        raise HTTPException(status_code=401, detail="Nutricionista não logado")
    
    prato = PratoController.editarPrato(idPrato, novo_prato)
    if prato is None:
        raise HTTPException(status_code=404, detail="Prato não encontrado")
    return prato