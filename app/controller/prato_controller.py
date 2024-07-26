from app.models.prato import Prato, PratoRequest

class PratoController:
    listaPratos = []
    id_counter = 1

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