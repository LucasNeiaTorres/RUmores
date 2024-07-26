from pydantic import BaseModel, Field

class UsuarioRequest(BaseModel):
    nome: str = Field(..., example="Bruno Aziz Spring")
    
    def getNome(self):
        return self.nome
    
    def setNome(self, nome: str):
        self.nome = nome

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