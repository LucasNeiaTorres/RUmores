from pydantic import BaseModel, Field
from typing import Literal

class Refeicao(BaseModel):
    idRefeicao: int = Field(..., example=1)
    horario: Literal["Café da manhã", "Almoço", "Janta"] = Field(..., example="Almoço")
    idCardapio: int = Field(..., example=1)
     
    def getHorario(self):
        return self.horario   
     
    def setHorario(self, horario: Literal["Café da manhã", "Almoço", "Janta"]):   
        self.horario = horario
        
    def getIdCardapio(self):
        return self.idCardapio
    
    def setIdCardapio(self, idCardapio: int):
        self.idCardapio = idCardapio
        
    def getIdRefeicao(self):
        return self.idRefeicao
    
    def setIdRefeicao(self, idRefeicao: int):
        self.idRefeicao = idRefeicao
        