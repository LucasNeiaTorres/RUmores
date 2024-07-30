from fastapi import APIRouter, HTTPException
from app.models.usuario import Usuario, UsuarioRequest
from app.controller.usuario_controller import UsuarioController

router = APIRouter(
    prefix="/usuario",
    tags=["usuario"],
)

@router.post("/login", response_model=Usuario)
async def inserirLogin(usuario: UsuarioRequest):
    user = UsuarioController.login(usuario)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user

# TODO: 
# - tira algumas rotas de estudante e nutricionista e coloca aqui