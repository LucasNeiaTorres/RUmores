from fastapi import APIRouter, HTTPException
from app.models.usuario import Usuario, UsuarioRequest
from app.controller.usuario_controller import UsuarioController
from app.controller.cardapio_controller import CardapioController
from app.models.cardapio import Cardapio, CardapioRequest
from app.models.prato import Prato, PratoRequest
from typing import List


from app.controller.refeicao_controller import RefeicaoController
from app.models.refeicao import Refeicao, RefeicaoRequest

from app.controller.refeicaoPrato_controller import RefeicaoPratoController
from app.controller.prato_controller import PratoController
from app.models.refeicaoPrato import RefeicaoPrato, RefeicaoPratoRequest
from app.views.prato_view import selecionaPrato as sp, adicionarPrato as ap, obterListaPratos, editarPrato as ep

from datetime import date


router = APIRouter(
    prefix="/AdicionarInfoNutricionais",
    tags=["Adicionar Informações Nutricionais"],
)

@router.get("/pratos/", response_model=List[Prato])
async def gerenciamentoPratos():
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