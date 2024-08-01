from app.models.usuario import Usuario, UsuarioRequest, LoginRequest
from app.models.usuario import Estudante, Nutricionista
from typing import List, Union

class UsuarioController:
    listaUsuarios: List[Union[Estudante, Nutricionista]] = [
        Estudante(idUsuario=1, tipo="Estudante", nome="Bruno Aziz Spring", email="bruninho@gmail.com", senha="123456", grr="GRR20200000"),
        Estudante(idUsuario=2, tipo="Estudante", nome="Estudante Aziz Spring", email="estudante@gmail.com", senha="123456", grr="GRR20200001"),
        Nutricionista(idUsuario=3, tipo="Nutricionista", nome="Nutri Aziz Spring", email="nutri@gmail.com", senha="123456", crn="CRN20200000"),
        Nutricionista(idUsuario=4, tipo="Nutricionista", nome="Nutri2 Aziz Spring", email="nutr2@gmail.com", senha="123456", crn="CRN20200001")
    ]
    id_counter = 5
    usuario_logado: Union[Estudante, Nutricionista] = None
    
    @classmethod
    def login(cls, usuario: LoginRequest):
        for user in cls.listaUsuarios:
            if user.getEmail() == usuario.getEmail() and user.getSenha() == usuario.getSenha():
                cls.usuario_logado = user
                return user
        return None
    
    @classmethod
    def adicionarUsuario(cls, usuario: Union[Estudante, Nutricionista]):
        cls.id_counter += 1
        cls.listaUsuarios.append(usuario)
        return usuario
    
    @classmethod
    def getIdCounter(cls):
        return cls.id_counter
    
    @classmethod
    def getUsuario(cls, idUsuario: int):
        for usuario in cls.listaUsuarios:
            if usuario.getIdUsuario() == idUsuario:
                return usuario
        return None
    
    
    @classmethod
    def getUsuarioLogado(cls):
        return cls.usuario_logado
    
    # @classmethod
    # def editarUsuario(cls, idUsuario: int, novo_usuario: UsuarioRequest):
    #     usuario = cls.getUsuario(idUsuario)
    #     if usuario is None:
    #         return None
    #     usuario.nome = novo_usuario.nome
    #     usuario.email = novo_usuario.email
    #     usuario.senha = novo_usuario.senha
    #     return usuario
    
    @classmethod
    def removeUsuario(cls, idUsuario: int):
        for usuario in cls.listaUsuarios:
            if usuario.getIdUsuario() == idUsuario:
                cls.listaUsuarios.remove(usuario)
                return usuario
        return None
    
    @classmethod
    def getListaUsuarios(cls):
        if len(cls.listaUsuarios) == 0:
            return []
        return cls.listaUsuarios