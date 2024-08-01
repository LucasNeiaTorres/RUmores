from pydantic import BaseModel, Field
from datetime import date
from typing import Literal

class AvaliacaoRequest(BaseModel):
    data: date = Field(..., example="2024-05-05")
    nota: int = Field(..., example=1, min=1, max=5)
    comentario: str = Field(..., example="Estava ótimo")
    
    def getIdPrato(self):
        return self.data
    
    def setData(self, data: date):
        self.data = data
        
    def getNota(self):
        return self.nota
    
    def setNota(self, nota: int):
        self.nota = nota
        
    def getComentario(self):
        return self.comentario
    
    def setComentario(self, comentario: str):
        self.comentario = comentario
        
    
class Avaliacao(AvaliacaoRequest):
    idAvaliacao: int = Field(..., example=1)
    idPrato: int = Field(..., example=1)
    idUsuario: int = Field(..., example=1)

    
    def getIdAvaliacao(self):
        return self.idAvaliacao
    
    def setIdAvaliacao(self, idAvaliacao: int):
        self.idAvaliacao = idAvaliacao
                
    def getIdPrato(self):
        return self.idPrato
    
    def setIdPrato(self, idPrato: int):
        self.idPrato = idPrato
        
    def getIdUsuario(self):
        return self.idUsuario
    
    def setIdUsuario(self, idUsuario: int):
        self.idUsuario = idUsuario