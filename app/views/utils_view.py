from fastapi import APIRouter, HTTPException
from typing import List
from app.models.usuario import Usuario
from app.models.cardapio import Cardapio
from app.controller.usuario_controller import UsuarioController
from app.controller.cardapio_controller import CardapioController

router = APIRouter(
    prefix="/utils",
    tags=["utils"],
)

@router.get("/users/", response_model=List[Usuario])
async def ObterListaUsuarios():
    usuarioList = UsuarioController.getListaUsuarios()
    return usuarioList

@router.get("/calendario/", response_model=List[Cardapio])
async def ObterListaCardapios():
    cardapioList = CardapioController.getListaCardapio() 
    return cardapioList