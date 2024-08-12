from fastapi import APIRouter, HTTPException
from app.controller.prato_controller import PratoController
from app.controller.usuario_controller import UsuarioController
from app.models.prato import Prato
from app.models.avaliacao import Avaliacao, AvaliacaoRequest
from app.models.usuario import Estudante
from app.controller.avaliacao_controller import AvaliacaoController


router = APIRouter(
    prefix="/RegistrarReviewPrato",
    tags=["Registrar Review de Prato"],
)

@router.post("/login_aluno", response_model=Estudante)
async def loginAluno(email: str, senha: str):
    user = UsuarioController.login(email, senha)
    if user is None or user.getTipo() != "Estudante":
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return user

@router.get("/pratos/")
async def pratosParaAvaliar():
    if UsuarioController.getUsuarioLogado() is None or UsuarioController.getUsuarioLogado().getTipo() != "Estudante":
        raise HTTPException(status_code=401, detail="Aluno não logado")
    pratoList = PratoController.getListaPratos() 
    if pratoList is None:
        raise HTTPException(status_code=404, detail="Pratos não encontrados")
    return pratoList


@router.get("/prato/{idPrato}", response_model=Prato)
async def selecionaPrato(idPrato: int):
    if UsuarioController.getUsuarioLogado() is None or UsuarioController.getUsuarioLogado().getTipo() != "Estudante":
        raise HTTPException(status_code=401, detail="Aluno não logado")
    prato = PratoController.selecionarPrato(idPrato)
    if prato is None:
        raise HTTPException(status_code=404, detail="Prato não encontrado")
    return prato

@router.post("/avaliacao/", response_model=Avaliacao)
async def insereAvaliacao(avaliacao: AvaliacaoRequest):
    prato_selecionado = PratoController.getPratoSelecionado()
    if prato_selecionado is None:
        raise HTTPException(status_code=404, detail="Prato não encontrado")
    
    nova_avaliacao = AvaliacaoController.adicionarAvaliacao(avaliacao, prato_selecionado)
    if nova_avaliacao is None:
        raise HTTPException(status_code=404, detail="Estudante ou prato não encontrado")
    return nova_avaliacao