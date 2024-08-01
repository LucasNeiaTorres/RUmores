from app.models.avaliacao import Avaliacao, AvaliacaoRequest
from app.controller.estudante_controller import EstudanteController
from app.controller.usuario_controller import UsuarioController
from app.controller.prato_controller import PratoController

class AvaliacaoController:
    listaAvaliacoes = [
        Avaliacao(idAvaliacao=1,data="2024-11-01", idUsuario=1, idPrato=1, nota=5, comentario="Muito bom!"),
        Avaliacao(idAvaliacao=6,data="2024-11-01", idUsuario=2, idPrato=1, nota=4, comentario="Muito ok!"),
        Avaliacao(idAvaliacao=7,data="2024-11-01", idUsuario=3, idPrato=1, nota=5, comentario="Já comi melhores."),
        Avaliacao(idAvaliacao=2,data="2024-11-01", idUsuario=2, idPrato=2, nota=4, comentario="Bom!"),
        Avaliacao(idAvaliacao=3,data="2024-11-01", idUsuario=3, idPrato=3, nota=3, comentario="Regular!"),
        Avaliacao(idAvaliacao=4,data="2024-11-01", idUsuario=4, idPrato=4, nota=2, comentario="Ruim!"),
        Avaliacao(idAvaliacao=8,data="2024-11-01", idUsuario=3, idPrato=4, nota=5, comentario="A tia da cantina é muito legal! Comi muito!"),
        Avaliacao(idAvaliacao=5,data="2024-11-01", idUsuario=5, idPrato=5, nota=1, comentario="Muito ruim!")]
    id_counter = 9

    @classmethod
    def adicionarAvaliacao(cls, avaliacao: AvaliacaoRequest, idPrato: int):
        if not UsuarioController.getUsuarioLogado():
            return None
        if not PratoController.getPrato(idPrato):
            return None
        nova_avaliacao = Avaliacao(idAvaliacao=cls.id_counter, idPrato=idPrato, **avaliacao.dict())
        cls.id_counter += 1
        cls.listaAvaliacoes.append(nova_avaliacao)
        return nova_avaliacao
    
    @classmethod
    def getListaAvaliacoes(cls):
        if len(cls.listaAvaliacoes) == 0:
            return []
        return cls.listaAvaliacoes
    
    @classmethod
    def getAvaliacao(cls, idAvaliacao: int):
        for avaliacao in cls.listaAvaliacoes:
            if avaliacao.idAvaliacao == idAvaliacao:
                return avaliacao
        return None
    
    @classmethod
    def editarAvaliacao(cls, idAvaliacao: int, nova_avaliacao: AvaliacaoRequest, idPrato: int):
        avaliacao = cls.getAvaliacao(idAvaliacao)
        if avaliacao is None:
            return None
        if not EstudanteController.getEstudante(nova_avaliacao.idUsuario):
            return None
        if not PratoController.getPrato(idPrato):
            return None
        avaliacao.nota = nova_avaliacao.nota
        avaliacao.comentario = nova_avaliacao.comentario
        avaliacao.idUsuario = nova_avaliacao.idUsuario
        return avaliacao
    
    @classmethod
    def removeAvaliacao(cls, idAvaliacao: int):
        for avaliacao in cls.listaAvaliacoes:
            if avaliacao.idAvaliacao == idAvaliacao:
                cls.listaAvaliacoes.remove(avaliacao)
                return avaliacao
        return None