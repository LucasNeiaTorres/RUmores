from app.models.usuario import Nutricionista, UsuarioRequest

class NutricionistaController:
    listaNutricionistas = []
    id_counter = 1
    
    @classmethod    
    def adicionarNutricionista(cls, nutricionista: UsuarioRequest):
        novo_nutricionista = Nutricionista(idUsuario=cls.id_counter, tipo="nutricionista", **nutricionista.dict())
        cls.id_counter += 1
        cls.listaNutricionistas.append(novo_nutricionista)
        return novo_nutricionista
    
    @classmethod
    def getNutricionista(cls, idUsuario: int):
        for nutricionista in cls.listaNutricionistas:
            if nutricionista.idUsuario == idUsuario:
                return nutricionista
        return None
    
    @classmethod
    def editarNutricionista(cls, idUsuario: int, novo_nutricionista: UsuarioRequest):
        nutricionista = cls.getNutricionista(idUsuario)
        if nutricionista is None:
            return None
        nutricionista.nome = novo_nutricionista.nome
        return nutricionista
    
    @classmethod
    def removeNutricionista(cls, idUsuario: int):
        for nutricionista in cls.listaNutricionistas:
            if nutricionista.idUsuario == idUsuario:
                cls.listaNutricionistas.remove(nutricionista)
                return nutricionista
        return None
    
    @classmethod
    def getListaNutricionistas(cls):
        if len(cls.listaNutricionistas) == 0:
            return []
        return cls.listaNutricionistas