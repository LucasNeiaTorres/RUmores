from fastapi import APIRouter, HTTPException
from typing import List
from app.models.prato import Prato, ListaPrato

router = APIRouter(
    prefix="/prato",
    tags=["prato"],
)

listaPratos = ListaPrato(pratos=[])

@router.get("/")
async def read_pratos():
    return listaPratos

@router.post("/")
async def create_prato(prato: Prato):
    listaPratos.adicionaPrato(prato)
    return prato