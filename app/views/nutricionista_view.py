# from fastapi import APIRouter, HTTPException
# from typing import List
# from app.models.usuario import Nutricionista
# from app.controller.nutricionista_controller import NutricionistaController

# router = APIRouter(
#     prefix="/nutricionista",
#     tags=["nutricionista"],
# )

# # @router.post("/", response_model=Nutricionista)
# # async def adicionarNutricionista(nutricionista: NutricionistaRequest):
# #     novo_nutricionista = NutricionistaController.adicionarNutricionista(nutricionista)
# #     return novo_nutricionista

# # @router.put("/{idUsuario}", response_model=Nutricionista)
# # async def editarNutricionista(idUsuario: int, novo_nutricionista: NutricionistaRequest):
# #     nutricionista = NutricionistaController.editarNutricionista(idUsuario, novo_nutricionista)
# #     if nutricionista is None:
# #         raise HTTPException(status_code=404, detail="Nutricionista não encontrado")
# #     return nutricionista

# # @router.get("/", response_model=List[Nutricionista])
# # async def ObterListaNutricionistas():
# #     nutricionistaList = NutricionistaController.getListaNutricionistas()
# #     return nutricionistaList