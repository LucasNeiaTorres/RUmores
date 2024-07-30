from fastapi import APIRouter, HTTPException
from app.models.usuario import Usuario, UsuarioRequest
from app.controller.usuario_controller import UsuarioController
from app.controller.cardapio_controller import CardapioController
from app.controller.prato_controller import PratoController

from app.models.cardapio import Cardapio, CardapioRequest
from app.models.prato import Prato
from app.models.avaliacao import Avaliacao, AvaliacaoRequest
from typing import List


from app.controller.refeicao_controller import RefeicaoController
from app.models.refeicao import Refeicao, RefeicaoRequest

from app.controller.refeicaoPrato_controller import RefeicaoPratoController
from app.models.refeicaoPrato import RefeicaoPrato, RefeicaoPratoRequest
from app.views.prato_view import obterListaPratos, selecionaPrato as sp
from app.views.avaliacao_view import adicionarAvaliacao as addAvaliacao

from datetime import date


router = APIRouter(
    prefix="/AdicionarInfoNutricionais",
    tags=["Adicionar Informacoes Nutricionais"],
)

@router.get("/pratos/")
async def pratosParaAvaliar():
    pratoList = await obterListaPratos()
    return pratoList


@router.get("/prato/{idPrato}", response_model=Prato)
async def selecionaPrato(idPrato: int):
    prato = await sp(idPrato)
    if prato is None:
        raise HTTPException(status_code=404, detail="Prato não encontrado")
    return prato

@router.post("/avaliacao/", response_model=Avaliacao)
async def adicionarAvaliacao(avaliacao: AvaliacaoRequest):
    prato_selecionado = PratoController.getPratoSelecionado()
    if prato_selecionado is None:
        raise HTTPException(status_code=404, detail="Prato não encontrado")

    nova_avaliacao = await addAvaliacao(avaliacao, prato_selecionado)
    if nova_avaliacao is None:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    return nova_avaliacao