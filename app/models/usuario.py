from pydantic import BaseModel, Field

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
    
    def getIdUsuario(self):
        return self.idUsuario
    
    def setIdUsuario(self, idUsuario: int):
        self.idUsuario = idUsuario
    
class Estudante(Usuario):
    tipo: str = Field("estudante")

class Nutricionista(Usuario):
    tipo: str = Field("nutricionista")