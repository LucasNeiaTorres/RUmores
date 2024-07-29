from app.models.refeicao import Refeicao, RefeicaoRequest

class RefeicaoController:
    listaRefeicao = []
    id_counter = 1
    
    @classmethod
    def adicionarRefeicao(cls, refeicao: RefeicaoRequest):
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