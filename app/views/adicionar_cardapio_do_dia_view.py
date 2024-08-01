from fastapi import APIRouter, HTTPException
from app.models.usuario import Nutricionista, LoginRequest
from app.views.usuario_view import inserirLogin
from app.controller.cardapio_controller import CardapioController
from app.controller.usuario_controller import UsuarioController
from datetime import date

router = APIRouter(
    prefix="/AdicionarCardapioDia",
    tags=["Adicionar Cardápio do Dia"],
)

@router.post("/login_nutricionista", response_model=Nutricionista)
async def loginNutricionista(nutricionista: LoginRequest):
    user = await inserirLogin(nutricionista)
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
    lista_cardapios = [cardapio.getData() for cardapio in lista_cardapios]
    return lista_cardapios

@router.post("/calendario/{ano}/{mes}/{dia}")
async def escolherData(ano: int, mes: int, dia: int):
    if UsuarioController.getUsuarioLogado() is None or UsuarioController.getUsuarioLogado().getTipo() != "Nutricionista":
        raise HTTPException(status_code=401, detail="Nutricionista não logado")
    data = date(ano, mes, dia)
    lista_pratos = CardapioController.abrirCardapioDia(data)
    # TODO: INSERE CARDAPIO_SELECIONADO
    if lista_pratos is None:
        raise HTTPException(status_code=404, detail="Sem pratos cadastrados")
    return lista_pratos