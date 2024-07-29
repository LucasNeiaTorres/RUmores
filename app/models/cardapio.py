from pydantic import BaseModel, Field
from datetime import date

class CardapioRequest(BaseModel):
    data: date = Field(..., example="2024-05-05")
     
    def getData(self):
        return self.data
    
    def setData(self, data: date):
        self.data = data
    
class Cardapio(CardapioRequest):
    idCardapio: int = Field(..., example=1)
    
    def getIdCardapio(self):
        return self.idCardapio
    
    def setIdCardapio(self, idCardapio: int):
        self.idCardapio = idCardapio