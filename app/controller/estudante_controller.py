from app.models.usuario import Estudante, UsuarioRequest, EstudanteRequest
from app.controller.usuario_controller import UsuarioController

class EstudanteController:
    
    @classmethod
    def adicionarEstudante(cls, estudante: EstudanteRequest):
        idUsuario = UsuarioController.getIdCounter()
        novo_estudante = Estudante(idUsuario=idUsuario, tipo="Estudante", **estudante.dict())
        UsuarioController.adicionarUsuario(novo_estudante)
        return novo_estudante
    
    # @classmethod
    # def editarEstudante(cls, idUsuario: int, novo_estudante: UsuarioRequest):
    #     estudante = cls.getEstudante(idUsuario)
    #     if estudante is None:
    #         return None
    #     estudante.nome = novo_estudante.nome
    #     return estudante