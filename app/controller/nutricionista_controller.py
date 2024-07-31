from app.models.usuario import Nutricionista, UsuarioRequest
from app.controller.usuario_controller import UsuarioController

class NutricionistaController:
    listaNutricionistas = []
    id_counter = 1
    
    @classmethod    
    def adicionarNutricionista(cls, nutricionista: UsuarioRequest):
        idUsuario = UsuarioController.getIdCounter()
        novo_nutricionista = Nutricionista(idUsuario=idUsuario, tipo="Nutricionista", **nutricionista.dict())
        UsuarioController.adicionarUsuario(novo_nutricionista)
        return novo_nutricionista
    
    # @classmethod
    # def editarNutricionista(cls, idUsuario: int, novo_nutricionista: UsuarioRequest):
    #     nutricionista = cls.getNutricionista(idUsuario)
    #     if nutricionista is None:
    #         return None
    #     nutricionista.nome = novo_nutricionista.nome
    #     return nutricionista
    