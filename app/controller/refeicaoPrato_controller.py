from app.models.refeicaoPrato import RefeicaoPrato, RefeicaoPratoRequest
from app.controller.prato_controller import PratoController
from app.controller.refeicao_controller import RefeicaoController

class RefeicaoPratoController:
    listaRefeicaoPrato = []
    id_counter = 1
    
    @classmethod   
    def adicionarRefeicaoPrato(cls, refeicaoPrato: RefeicaoPratoRequest):
        if not PratoController.getPrato(refeicaoPrato.idPrato):
            return None
        if not RefeicaoController.getRefeicao(refeicaoPrato.idRefeicao):
            return None
        novo_refeicaoPrato = RefeicaoPrato(idRefeicaoPrato=cls.id_counter, **refeicaoPrato.dict())
        cls.id_counter += 1
        cls.listaRefeicaoPrato.append(novo_refeicaoPrato)
        return novo_refeicaoPrato
    
    @classmethod
    def getListaRefeicaoPrato(cls):
        if len(cls.listaRefeicaoPrato) == 0:
            return []
        return cls.listaRefeicaoPrato
    
    @classmethod
    def getRefeicaoPrato(cls, idRefeicaoPrato: int):
        for refeicaoPrato in cls.listaRefeicaoPrato:
            if refeicaoPrato.idRefeicaoPrato == idRefeicaoPrato:
                return refeicaoPrato
        return None
    
    @classmethod
    def editarRefeicaoPrato(cls, idRefeicaoPrato: int, novo_refeicaoPrato: RefeicaoPratoRequest):
        refeicaoPrato = cls.getRefeicaoPrato(idRefeicaoPrato)
        if refeicaoPrato is None:
            return None
        if not PratoController.getPrato(novo_refeicaoPrato.idPrato):
            return None
        if not RefeicaoController.getRefeicao(novo_refeicaoPrato.idRefeicao):
            return None
        refeicaoPrato.idPrato = novo_refeicaoPrato.idPrato
        refeicaoPrato.idRefeicao = novo_refeicaoPrato.idRefeicao
        return refeicaoPrato
    
    @classmethod
    def removeRefeicaoPrato(cls, idRefeicaoPrato: int):
        for refeicaoPrato in cls.listaRefeicaoPrato:
            if refeicaoPrato.idRefeicaoPrato == idRefeicaoPrato:
                cls.listaRefeicaoPrato.remove(refeicaoPrato)
                return refeicaoPrato
        return None
    
    @classmethod
    def getRefeicaoPratoByRefeicao(cls, idRefeicao: int):
        refeicaoPratoList = []
        for refeicaoPrato in cls.listaRefeicaoPrato:
            if refeicaoPrato.idRefeicao == idRefeicao:
                refeicaoPratoList.append(refeicaoPrato)
        return refeicaoPratoList