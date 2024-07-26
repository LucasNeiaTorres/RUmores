from fastapi import APIRouter, HTTPException
from typing import List
from app.models.usuario import Estudante, UsuarioRequest
from app.controller.estudante_controller import EstudanteController

router = APIRouter(
    prefix="/estudante",
    tags=["estudante"],
)

@router.post("/", response_model=Estudante)
async def adicionarEstudante(estudante: UsuarioRequest):
    novo_estudante = EstudanteController.adicionarEstudante(estudante)
    return novo_estudante

@router.get("/{idUsuario}", response_model=Estudante)
async def selecionaEstudante(idUsuario: int):
    estudante = EstudanteController.getEstudante(idUsuario)
    if estudante is None:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    return estudante

@router.put("/{idUsuario}", response_model=Estudante)
async def editarEstudante(idUsuario: int, novo_estudante: UsuarioRequest):
    estudante = EstudanteController.editarEstudante(idUsuario, novo_estudante)
    if estudante is None:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    return estudante

@router.delete("/{idUsuario}")
async def excluirEstudante(idUsuario: int):
    estudante = EstudanteController.removeEstudante(idUsuario)
    if estudante is None:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    return estudante

@router.get("/", response_model=List[Estudante])
async def ObterListaEstudantes():
    estudanteList = EstudanteController.getListaEstudantes()
    return estudanteList