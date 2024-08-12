from pydantic import BaseModel, Field

class PratoRequest(BaseModel):
    nome: str = Field(..., example="Strogonoff de Carne")
    informacao_nutricional: str = Field(..., example="125 kcal")
    # ter classe informacao_nutricional?
    
    def getNome(self):
        return self.nome
    
    def setNome(self, nome: str):
        self.nome = nome
    
    def getInformacaoNutricional(self):
        return self.informacao_nutricional
    
    def setInformacaoNutricional(self, info_nutri: str):
        self.informacao_nutricional = info_nutri
class Prato(PratoRequest):
    idPrato: int = Field(..., example=1)
    
    def getIdPrato(self):
        return self.idPrato
    
    def setIdPrato(self, idPrato: int):
        self.idPrato = idPrato
    