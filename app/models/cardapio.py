from pydantic import BaseModel, Field
from datetime import date
from typing import List, Literal
from app.models.prato import Prato

class CardapioRequest(BaseModel):
    data: date = Field(..., example="2024-05-05")
    horario: Literal["Café da manhã", "Almoço", "Janta"] = Field(..., example="Almoço")
    pratos: List[Prato] # Faz tabela associativa
    
    def getData(self):
        return self.data
    
    def setData(self, data: date):
        self.data = data
        
    def getHorario(self):
        return self.horario   
    
    def setHorario(self, horario: Literal["Café da manhã", "Almoço", "Janta"]):   
        self.horario = horario
        
    def getPratos(self):
        return self.pratos
    
    def setPratos(self, pratos: List[Prato]):
        self.pratos = pratos
    
class Cardapio(CardapioRequest):
    idCardapio: int = Field(..., example=1)
    
    def getIdCardapio(self):
        return self.idCardapio