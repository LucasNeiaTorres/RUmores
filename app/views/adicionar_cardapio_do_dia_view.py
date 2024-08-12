from fastapi import APIRouter, HTTPException
from app.models.usuario import Nutricionista
from app.controller.cardapio_controller import CardapioController
from app.controller.usuario_controller import UsuarioController
from app.controller.prato_controller import PratoController
from app.controller.refeicaoPrato_controller import RefeicaoPratoController
from app.controller.refeicao_controller import RefeicaoController
from datetime import date
from typing import Literal


router = APIRouter(
    prefix="/AdicionarCardapioDia",
    tags=["Adicionar Cardápio do Dia"],
)

@router.post("/login_nutricionista", response_model=Nutricionista)
async def loginNutricionista(email: str, senha: str):
    user = UsuarioController.login(email, senha)
    if user is None or user.getTipo() != "Nutricionista":
        raise HTTPException(status_code=404, detail="Nutricionista não encontrado")
    return user

@router.get("/calendario/")
async def abrirCalendario():
    if UsuarioController.getUsuarioLogado() is None or UsuarioController.getUsuarioLogado().getTipo() != "Nutricionista":
        raise HTTPException(status_code=401, detail="Nutricionista não logado")
    lista_cardapios = CardapioController.getListaCardapio()
    if lista_cardapios is None:
        raise HTTPException(status_code=404, detail="Sem cardápios cadastrados")
    return lista_cardapios

@router.post("/calendario/{data}")
async def escolherData(data: date):
    """
    Seleciona a data do cardápio
    """
    if UsuarioController.getUsuarioLogado() is None or UsuarioController.getUsuarioLogado().getTipo() != "Nutricionista":
        raise HTTPException(status_code=401, detail="Nutricionista não logado")
    lista_pratos = CardapioController.abrirCardapioDia(data)
    
    if lista_pratos is None:
        raise HTTPException(status_code=404, detail="Sem pratos cadastrados")
    return lista_pratos

@router.get("/pratos/")
async def listaPratos():
    if UsuarioController.getUsuarioLogado() is None or UsuarioController.getUsuarioLogado().getTipo() != "Nutricionista":
        raise HTTPException(status_code=401, detail="Nutricionista não logado")
    pratos = PratoController.getListaPratos()
    if pratos is None:
        raise HTTPException(status_code=404, detail="Pratos não encontrados")
    pratos = [prato.getNome() for prato in pratos]
    return pratos

@router.post("/calendario/selecionar-prato/")
async def atribuirPratoCardapio(nome_prato: str, horario_refeicao: Literal["Café da manhã", "Almoço", "Jantar"]):
    if UsuarioController.getUsuarioLogado() is None or UsuarioController.getUsuarioLogado().getTipo() != "Nutricionista":
        raise HTTPException(status_code=401, detail="Nutricionista não logado")
    
    lista_pratos = CardapioController.atribuirPratoCardapio(nome_prato, horario_refeicao)
    if lista_pratos is None:
        raise HTTPException(status_code=404, detail="Erro ao atribuir prato")
    return lista_pratos


# @router.post("/calendario/adicionar-prato/")
# async def adicionarPrato(prato: PratoRequest, horario_refeicao: Literal["Café da manhã", "Almoço", "Jantar"]):
#     if UsuarioController.getUsuarioLogado() is None or UsuarioController.getUsuarioLogado().getTipo() != "Nutricionista":
#         raise HTTPException(status_code=401, detail="Nutricionista não logado")
    
#     cardapio = CardapioController.getCardapioSelecionado()
#     if cardapio is None:
#         raise HTTPException(status_code=401, detail="Cardápio não selecionado")
    
#     prato = PratoController.getPratoByNome(nome_prato)
#     if prato is None:
#         raise HTTPException(status_code=404, detail="Prato não encontrado")
    
#     ref = CardapioController.getRefeicaoCardapio(horario_refeicao, cardapio)
#     # verifica se refeição já existe
#     if ref is None:
#         # adiciona refeicao se não existe
#         ref = RefeicaoController.adicionarRefeicao(RefeicaoRequest(horario=horario_refeicao, idCardapio=cardapio))
    
#     if RefeicaoPratoController.isPratoInRefeicao(prato.getIdPrato(), ref.getIdRefeicao()):
#         raise HTTPException(status_code=404, detail="Prato já cadastrado nessa refeição")
#     else:
#         RefeicaoPratoController.adicionarRefeicaoPrato(RefeicaoPratoRequest(idPrato=prato.getIdPrato(), idRefeicao=ref.getIdRefeicao()))
#     lista_pratos = CardapioController.abrirCardapioDia(CardapioController.getDataCardapioSelecionado())
#     return lista_pratos

