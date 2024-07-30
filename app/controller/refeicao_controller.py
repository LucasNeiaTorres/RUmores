from app.models.refeicao import Refeicao, RefeicaoRequest
from app.controller.cardapio_controller import CardapioController

class RefeicaoController:
    listaRefeicao = [Refeicao(idRefeicao=1, idCardapio=1, horario="Almoço"),
                        Refeicao(idRefeicao=2, idCardapio=1, horario="Janta"),
                        Refeicao(idRefeicao=3, idCardapio=1, horario="Café da manhã"),
                        Refeicao(idRefeicao=4, idCardapio=2, horario="Almoço"),
                        Refeicao(idRefeicao=5, idCardapio=2, horario="Janta"),
                        Refeicao(idRefeicao=6, idCardapio=2, horario="Café da manhã"),
                        Refeicao(idRefeicao=7, idCardapio=3, horario="Almoço"),
                        Refeicao(idRefeicao=8, idCardapio=3, horario="Janta"),
                        Refeicao(idRefeicao=9, idCardapio=3, horario="Café da manhã"),
                        Refeicao(idRefeicao=10, idCardapio=4, horario="Almoço"),
                        Refeicao(idRefeicao=11, idCardapio=4, horario="Janta"),
                        Refeicao(idRefeicao=12, idCardapio=4, horario="Café da manhã"),
                        Refeicao(idRefeicao=13, idCardapio=5, horario="Almoço"),
                        Refeicao(idRefeicao=14, idCardapio=5, horario="Janta"),
                        Refeicao(idRefeicao=15, idCardapio=5, horario="Café da manhã")]

                     
    id_counter = 16
    
    @classmethod
    def adicionarRefeicao(cls, refeicao: RefeicaoRequest):
        if not CardapioController.getCardapio(refeicao.idCardapio):
            return None
        nova_refeicao = Refeicao(idRefeicao=cls.id_counter, **refeicao.dict())
        cls.id_counter += 1
        cls.listaRefeicao.append(nova_refeicao)
        return nova_refeicao
    
    @classmethod
    def getListaRefeicao(cls):
        if len(cls.listaRefeicao) == 0:
            return []
        return cls.listaRefeicao
    
    @classmethod
    def getRefeicao(cls, idRefeicao: int):
        for refeicao in cls.listaRefeicao:
            if refeicao.idRefeicao == idRefeicao:
                return refeicao
        return None
    
    @classmethod
    def editarRefeicao(cls, idRefeicao: int, nova_refeicao: RefeicaoRequest):
        refeicao = cls.getRefeicao(idRefeicao)
        if refeicao is None:
            return None
        if not CardapioController.getCardapio(refeicao.idCardapio):
            return None
        refeicao.horario = nova_refeicao.horario
        return refeicao
    
    @classmethod 
    def removeRefeicao(cls, idRefeicao: int):
        for refeicao in cls.listaRefeicao:
            if refeicao.idRefeicao == idRefeicao:
                cls.listaRefeicao.remove(refeicao)
                return refeicao
        return None
    
    @classmethod
    def getRefeicaoByHorario(cls, horario: str):
        for refeicao in cls.listaRefeicao:
            if refeicao.horario == horario:
                return refeicao
        return None
    
    @classmethod
    def getRefeicaoByCardapio(cls, idCardapio: int):
        lista_refeicao = []
        for refeicao in cls.listaRefeicao:
            if refeicao.idCardapio == idCardapio:
                lista_refeicao.append(refeicao)
        return lista_refeicao