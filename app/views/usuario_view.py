from fastapi import APIRouter, HTTPException
from app.models.usuario import Usuario, UsuarioRequest, LoginRequest
from app.controller.usuario_controller import UsuarioController
from typing import List

router = APIRouter(
    prefix="/usuario",
    tags=["usuario"],
)

@router.post("/login", response_model=Usuario)
async def inserirLogin(usuario: LoginRequest):
    user = UsuarioController.login(usuario)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user

@router.get("/{idUsuario}", response_model=Usuario)
async def selecionaUsuario(idUsuario: int):
    usuario = UsuarioController.getUsuario(idUsuario)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@router.get("/", response_model=List[Usuario])
async def ObterListaUsuarios():
    usuarioList = UsuarioController.getListaUsuarios()
    return usuarioList


# TODO: 
# - tira algumas rotas de estudante e nutricionista e coloca aqui