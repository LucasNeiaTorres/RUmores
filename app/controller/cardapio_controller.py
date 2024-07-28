from app.models.cardapio import Cardapio, CardapioRequest

class CardapioController:
    listaCardapio = []
    id_counter = 1

    @classmethod
    def adicionarCardapio(cls, cardapio: CardapioRequest):
        novo_cardapio = Cardapio(idCardapio=cls.id_counter, **cardapio.dict())
        cls.id_counter += 1
        cls.listaCardapio.append(novo_cardapio)
        return novo_cardapio
    
    @classmethod
    def getListaCardapio(cls):
        if len(cls.listaCardapio) == 0:
            return []
        return cls.listaCardapio
    
    @classmethod
    def getCardapio(cls, idCardapio: int):
        for cardapio in cls.listaCardapio:
            if cardapio.idCardapio == idCardapio:
                return cardapio
        return None
    
    @classmethod
    def editarCardapio(cls, idCardapio: int, novo_cardapio: CardapioRequest):
        cardapio = cls.getCardapio(idCardapio)
        if cardapio is None:
            return None
        cardapio.data = novo_cardapio.data
        cardapio.horario = novo_cardapio.horario
        cardapio.pratos = novo_cardapio.pratos
        return cardapio
    
    @classmethod
    def removeCardapio(cls, idCardapio: int):
        for cardapio in cls.listaCardapio:
            if cardapio.idCardapio == idCardapio:
                cls.listaCardapio.remove(cardapio)
                return cardapio
        return None
    
    @classmethod
    def getCardapioByDate(cls, data: str):
        for cardapio in cls.listaCardapio:
            if cardapio.data == data:
                return cardapio
        return None