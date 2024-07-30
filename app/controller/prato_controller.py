from app.models.prato import Prato, PratoRequest

class PratoController:
    listaPratos = [Prato(idPrato=1, nome="Arroz", informacao_nutricional="Carboidrato"),
                   Prato(idPrato=2, nome="Feijão", informacao_nutricional="Proteína"),
                   Prato(idPrato=3, nome="Carne", informacao_nutricional="Proteína"),
                   Prato(idPrato=4, nome="Salada", informacao_nutricional="Vitaminas"),
                   Prato(idPrato=5, nome="Suco", informacao_nutricional="Vitaminas")]
    id_counter = 6
    prato_selecionado = None

    @classmethod
    def adicionarPrato(cls, prato: PratoRequest):
        novo_prato = Prato(idPrato=cls.id_counter, **prato.dict())
        cls.id_counter += 1
        cls.listaPratos.append(novo_prato)
        return novo_prato

    @classmethod
    def getListaPratos(cls):
        if len(cls.listaPratos) == 0:
            return []
        return cls.listaPratos 
    
    @classmethod
    def getPrato(cls, idPrato: int):
        for prato in cls.listaPratos:
            if prato.idPrato == idPrato:
                return prato
        return None
    
    @classmethod
    def editarPrato(cls, idPrato: int, novo_prato: PratoRequest):
        prato = cls.getPrato(idPrato)
        if prato is None:
            return None
        prato.nome = novo_prato.nome
        prato.informacao_nutricional = novo_prato.informacao_nutricional
        return prato
    
    @classmethod
    def removePrato(cls, idPrato: int):
        for prato in cls.listaPratos:
            if prato.idPrato == idPrato:
                cls.listaPratos.remove(prato)
                return prato
        return None

    @classmethod
    def selecionarPrato(cls, idPrato: int):
        prato = cls.getPrato(idPrato)
        if prato is None:
            return None
        cls.prato_selecionado = prato.idPrato
        return prato

    @classmethod
    def getPratoSelecionado(cls):
        return cls.prato_selecionado