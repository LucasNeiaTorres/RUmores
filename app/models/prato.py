from pydantic import BaseModel, Field
from typing import List

class Prato(BaseModel):
    nome: str = Field(..., example="Strogonoff")
    informacao_nutricional: str = Field(..., example="12 kcal")
    
class ListaPrato(BaseModel):
    pratos: List[Prato] = Field(..., example=[{"nome": "Strogonoff", "informacao_nutricional": "12 kcal"}])
    
    def adicionaPrato(self, prato: Prato):
        self.pratos.append(prato)
        return prato