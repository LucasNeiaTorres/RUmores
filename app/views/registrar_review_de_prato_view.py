from fastapi import APIRouter, HTTPException
from app.controller.prato_controller import PratoController
from app.controller.usuario_controller import UsuarioController
from app.models.prato import Prato
from app.models.avaliacao import Avaliacao, AvaliacaoRequest
from app.models.usuario import Estudante
from app.views.prato_view import obterListaPratos, selecionaPrato as sp
from app.views.avaliacao_view import adicionarAvaliacao as addAvaliacao
from app.views.usuario_view import inserirLogin


router = APIRouter(
    prefix="/RegistrarReviewPrato",
    tags=["Registrar Review de Prato"],
)

@router.post("/login_aluno", response_model=Estudante)
async def loginAluno(email: str, senha: str):
    user = await inserirLogin(email, senha)
    if user is None or user.getTipo() != "Estudante":
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return user

@router.get("/pratos/")
async def pratosParaAvaliar():
    if UsuarioController.getUsuarioLogado() is None or UsuarioController.getUsuarioLogado().getTipo() != "Estudante":
        raise HTTPException(status_code=401, detail="Aluno não logado")
    pratoList = await obterListaPratos()
    return pratoList


@router.get("/prato/{idPrato}", response_model=Prato)
async def selecionaPrato(idPrato: int):
    if UsuarioController.getUsuarioLogado() is None or UsuarioController.getUsuarioLogado().getTipo() != "Estudante":
        raise HTTPException(status_code=401, detail="Aluno não logado")
    prato = await sp(idPrato)
    if prato is None:
        raise HTTPException(status_code=404, detail="Prato não encontrado")
    return prato

@router.post("/avaliacao/", response_model=Avaliacao)
async def insereAvaliacao(avaliacao: AvaliacaoRequest):
    prato_selecionado = PratoController.getPratoSelecionado()
    if prato_selecionado is None:
        raise HTTPException(status_code=404, detail="Prato não encontrado")

    nova_avaliacao = await addAvaliacao(avaliacao, prato_selecionado)
    if nova_avaliacao is None:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    return nova_avaliacao