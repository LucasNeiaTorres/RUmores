from app.models.usuario import Estudante, UsuarioRequest

class EstudanteController:
    listaEstudantes = []
    id_counter = 1
    
    @classmethod
    def adicionarEstudante(cls, estudante: UsuarioRequest):
        novo_estudante = Estudante(idUsuario=cls.id_counter, tipo="estudante", **estudante.dict())
        cls.id_counter += 1
        cls.listaEstudantes.append(novo_estudante)
        return novo_estudante
    
    @classmethod
    def getEstudante(cls, idUsuario: int):
        for estudante in cls.listaEstudantes:
            if estudante.idUsuario == idUsuario:
                return estudante
        return None
    
    @classmethod
    def editarEstudante(cls, idUsuario: int, novo_estudante: UsuarioRequest):
        estudante = cls.getEstudante(idUsuario)
        if estudante is None:
            return None
        estudante.nome = novo_estudante.nome
        return estudante
    
    @classmethod
    def removeEstudante(cls, idUsuario: int):
        for estudante in cls.listaEstudantes:
            if estudante.idUsuario == idUsuario:
                cls.listaEstudantes.remove(estudante)
                return estudante
        return None
    
    @classmethod    
    def getListaEstudantes(cls):
        if len(cls.listaEstudantes) == 0:
            return []
        return cls.listaEstudantes