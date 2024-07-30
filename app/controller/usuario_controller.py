from app.models.usuario import Usuario, UsuarioRequest

class UsuarioController:
    listaUsuarios = []
    id_counter = 1
    
    @classmethod
    def login(cls, usuario: UsuarioRequest):
        for user in cls.listaUsuarios:
            if user.email == usuario.email and user.senha == usuario.senha:
                return user
        return None