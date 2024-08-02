from app.models.refeicaoPrato import RefeicaoPrato, RefeicaoPratoRequest
from app.controller.prato_controller import PratoController
from app.controller.refeicao_controller import RefeicaoController
from app.models.refeicao import Refeicao

class RefeicaoPratoController:
    listaRefeicaoPrato = [RefeicaoPrato(idRefeicaoPrato=1, idPrato=1, idRefeicao=1),
                          RefeicaoPrato(idRefeicaoPrato=2, idPrato=2, idRefeicao=1),
                          RefeicaoPrato(idRefeicaoPrato=5, idPrato=5, idRefeicao=1),
                            RefeicaoPrato(idRefeicaoPrato=6, idPrato=1, idRefeicao=2),
                            RefeicaoPrato(idRefeicaoPrato=7, idPrato=2, idRefeicao=2),
                            RefeicaoPrato(idRefeicaoPrato=8, idPrato=3, idRefeicao=2),
                            RefeicaoPrato(idRefeicaoPrato=10, idPrato=5, idRefeicao=2),
                            RefeicaoPrato(idRefeicaoPrato=11, idPrato=1, idRefeicao=3),
                            RefeicaoPrato(idRefeicaoPrato=15, idPrato=5, idRefeicao=3),
                            RefeicaoPrato(idRefeicaoPrato=16, idPrato=1, idRefeicao=4),
                            RefeicaoPrato(idRefeicaoPrato=17, idPrato=2, idRefeicao=4),
                            RefeicaoPrato(idRefeicaoPrato=20, idPrato=5, idRefeicao=4),
                            RefeicaoPrato(idRefeicaoPrato=21, idPrato=1, idRefeicao=5),
                            RefeicaoPrato(idRefeicaoPrato=22, idPrato=2, idRefeicao=5),
                            RefeicaoPrato(idRefeicaoPrato=25, idPrato=5, idRefeicao=5)
                        ]
    id_counter = 26
    
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

    @classmethod
    def getPratosByRefeicao(cls, refeicao: Refeicao):
        prato_list = []
        horario = refeicao.getHorario()
        for refeicaoPrato in cls.listaRefeicaoPrato:
            if refeicaoPrato.idRefeicao == refeicao.getIdRefeicao():
                prato = PratoController.getPrato(refeicaoPrato.getIdPrato())
                # prato_list.append({"nome":prato.nome,"id":prato.idPrato})
                prato_list.append(prato.getNome())
        return {"horario": horario, "pratos": prato_list}

    @classmethod
    def isPratoInRefeicao(cls, idPrato: int, idRefeicao: int):
        for refeicaoPrato in cls.listaRefeicaoPrato:
            print(refeicaoPrato.getIdPrato(), refeicaoPrato.getIdRefeicao())
            print(idPrato, idRefeicao)
            if refeicaoPrato.getIdPrato() == idPrato and refeicaoPrato.getIdRefeicao() == idRefeicao:
                return True
        return False