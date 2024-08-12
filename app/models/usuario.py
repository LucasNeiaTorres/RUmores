from pydantic import BaseModel, Field
from typing import Literal
                       
class UsuarioRequest(BaseModel):
    nome: str = Field(..., example="Bruno Aziz Spring")
    email: str = Field(..., example="bruninho@gmail.com")
    senha: str = Field(..., example="123456")
    
    def getNome(self):
        return self.nome
    
    def setNome(self, nome: str):
        self.nome = nome
        
    def getEmail(self):
        return self.email
    
    def setEmail(self, email: str):
        self.email = email
        
    def getSenha(self): 
        return self.senha
    
    def setSenha(self, senha: str):
        self.senha = senha

class Usuario(UsuarioRequest):
    idUsuario: int = Field(..., example=1)
    tipo: Literal["Estudante", "Nutricionista"] = Field(..., example="Estudante") 
    
    def getIdUsuario(self):
        return self.idUsuario
    
    def setIdUsuario(self, idUsuario: int):
        self.idUsuario = idUsuario
        
    def getTipo(self):
        return self.tipo
    
    def setTipo(self, tipo: Literal["Estudante", "Nutricionista"]):
        self.tipo = tipo
    
    
class Estudante(Usuario):
    grr: str = Field(..., example="GRR20200000")
    
    def getGrr(self):
        return self.grr
    
    def setGrr(self, grr: str):
        self.grr = grr
    
class Nutricionista(Usuario): 
    crn: str = Field(..., example="CRN20200000")
    
    def getCrn(self):
        return self.crn
    
    def setCrn(self, crn: str): 
        self.crn = crn