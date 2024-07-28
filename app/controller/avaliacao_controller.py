from app.models.avaliacao import Avaliacao, AvaliacaoRequest

class AvaliacaoController:
    listaAvaliacoes = []
    id_counter = 1
    
    @classmethod
    def adicionarAvaliacao(cls, avaliacao: AvaliacaoRequest):
        nova_avaliacao = Avaliacao(idAvaliacao=cls.id_counter, **avaliacao.dict())
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
    def editarAvaliacao(cls, idAvaliacao: int, nova_avaliacao: AvaliacaoRequest):
        avaliacao = cls.getAvaliacao(idAvaliacao)
        if avaliacao is None:
            return None
        avaliacao.nota = nova_avaliacao.nota
        avaliacao.comentario = nova_avaliacao.comentario
        return avaliacao
    
    @classmethod
    def removeAvaliacao(cls, idAvaliacao: int):
        for avaliacao in cls.listaAvaliacoes:
            if avaliacao.idAvaliacao == idAvaliacao:
                cls.listaAvaliacoes.remove(avaliacao)
                return avaliacao
        return None