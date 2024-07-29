from pydantic import BaseModel, Field

class RefeicaoPratoRequest(BaseModel):
    idPrato: int = Field(..., example=1)
    idRefeicao: int = Field(..., example=1)

    def getIdPrato(self):
        return self.idPrato
    
    def setIdPrato(self, idPrato: int):
        self.idPrato = idPrato
        
    def getIdRefeicao(self):
        return self.idRefeicao

    def setIdRefeicao(self, idRefeicao: int):
        self.idRefeicao = idRefeicao
    
class RefeicaoPrato(RefeicaoPratoRequest):
    idRefeicaoPrato: int = Field(..., example=1)
    
    def getIdRefeicaoPrato(self):
        return self.idRefeicaoPrato
    
    def setIdRefeicaoPrato(self, idRefeicaoPrato: int):
        self.idRefeicaoPrato = idRefeicaoPrato