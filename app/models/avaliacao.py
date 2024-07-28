from pydantic import BaseModel, Field
from datetime import date
from typing import Literal

class AvaliacaoRequest(BaseModel):
    data: date = Field(..., example="2024-05-05")
    idPrato: int = Field(..., example=1)
    estrelas: int = Field(..., example=1, min=1, max=5)
    descricao: str = Field(..., example="Estava ótimo")
    
    def getIdPrato(self):
        return self.data
    
    def setData(self, data: date):
        self.data = data
        
    def getIdPrato(self):
        return self.idPrato
    
    def setIdPrato(self, idPrato: int):
        self.idPrato = idPrato
        
    def getEstrelas(self):
        return self.estrelas
    
    def setEstrelas(self, estrelas: int):
        self.estrelas = estrelas
        
    def getDescricao(self):
        return self.descricao
    
    def setDescricao(self, descricao: str):
        self.descricao = descricao
    
class Avaliacao(AvaliacaoRequest):
    idAvaliacao: int = Field(..., example=1)
    
    def getIdAvaliacao(self):
        return self.idAvaliacao
    
    def setIdAvaliacao(self, idAvaliacao: int):
        self.idAvaliacao = idAvaliacao