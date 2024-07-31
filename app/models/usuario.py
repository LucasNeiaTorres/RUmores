from pydantic import BaseModel, Field
from typing import Literal

class LoginRequest(BaseModel):
    email: str = Field(..., example="bruninho@gmail.com")
    senha: str = Field(..., example="123456")
    
    def getEmail(self):
        return self.email
    
    def setEmail(self, email: str):
        self.email = email
        
    def getSenha(self):
        return self.senha
    
    def setSenha(self, senha: str):
        self.senha = senha
                       
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
    
class EstudanteRequest(UsuarioRequest):
    grr: str = Field(..., example="GRR20200000")
    
class Estudante(Usuario, EstudanteRequest):
    pass
class NutricionistaRequest(UsuarioRequest):
    crn: str = Field(..., example="CRN20200000")
    
class Nutricionista(Usuario, NutricionistaRequest):
    pass