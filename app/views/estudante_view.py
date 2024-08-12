# from fastapi import APIRouter, HTTPException
# from typing import List
# from app.models.usuario import Estudante
# from app.controller.estudante_controller import EstudanteController

# router = APIRouter(
#     prefix="/estudante",
#     tags=["estudante"],
# )

# # @router.post("/", response_model=Estudante)
# # async def adicionarEstudante(estudante: EstudanteRequest):
# #     novo_estudante = EstudanteController.adicionarEstudante(estudante)
# #     return novo_estudante


# # @router.put("/{idUsuario}", response_model=Estudante)
# # async def editarEstudante(idUsuario: int, novo_estudante: EstudanteRequest):
# #     estudante = EstudanteController.editarEstudante(idUsuario, novo_estudante)
# #     if estudante is None:
# #         raise HTTPException(status_code=404, detail="Estudante não encontrado")
# #     return estudante

# # @router.get("/", response_model=List[Estudante])
# # async def ObterListaEstudantes():
# #     estudanteList = EstudanteController.getListaEstudantes()
# #     return estudanteList
