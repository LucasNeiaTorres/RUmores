from fastapi import APIRouter, HTTPException
from app.models.usuario import Usuario, UsuarioRequest
from app.controller.usuario_controller import UsuarioController
from app.controller.cardapio_controller import CardapioController
from app.models.cardapio import Cardapio, CardapioRequest
from app.models.prato import Prato
from typing import List


from app.controller.refeicao_controller import RefeicaoController
from app.models.refeicao import Refeicao, RefeicaoRequest

from app.controller.refeicaoPrato_controller import RefeicaoPratoController
from app.controller.prato_controller import PratoController
from app.models.refeicaoPrato import RefeicaoPrato, RefeicaoPratoRequest
from app.views.prato_view import selecionaPrato as sp

from datetime import date


router = APIRouter(
    prefix="/AdicionarInfoNutricionais",
    tags=["Adicionar Informações Nutricionais"],
)

@router.get("/pratos/", response_model=List[Prato])
async def gerenciamentoPratos():
    pratos = PratoController.getListaPratos()
    if pratos is None:
        raise HTTPException(status_code=404, detail="Pratos não encontrados")
    return pratos

# TODO: 
# - tira algumas rotas de estudante e nutricionista e coloca aqui