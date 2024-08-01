from datetime import date
from app.models.cardapio import Cardapio, CardapioRequest

class CardapioController:
    listaCardapio = [Cardapio(idCardapio=1, data="2021-10-10"),
                     Cardapio(idCardapio=2, data="2021-10-11"),
                     Cardapio(idCardapio=3, data="2021-10-12"),
                     Cardapio(idCardapio=4, data="2021-10-13"),
                     Cardapio(idCardapio=5, data="2021-10-14")]
    id_counter = 6

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
        return cardapio
    
    @classmethod
    def removeCardapio(cls, idCardapio: int):
        for cardapio in cls.listaCardapio:
            if cardapio.idCardapio == idCardapio:
                cls.listaCardapio.remove(cardapio)
                return cardapio
        return None
    
    @classmethod
    def getCardapioByDate(cls, data: date):
        for cardapio in cls.listaCardapio:
            if cardapio.data == data:
                return cardapio
        return None
    
    @classmethod
    def abrirCardapioDia(cls, data: date):
        # importa aqui para não dar circular import
        from app.controller.refeicaoPrato_controller import RefeicaoPratoController
        from app.controller.refeicao_controller import RefeicaoController
        
        cardapio = cls.getCardapioByDate(data)
        if cardapio is None:
            return None
        
        lista_refeicao = RefeicaoController.getRefeicaoByCardapio(cardapio.getIdCardapio())

        lista_pratos = []

        for refeicao in lista_refeicao:
            lista_pratos.append(RefeicaoPratoController.getPratosByRefeicao(refeicao))

        return lista_pratos
    
    @classmethod 
    def abrirCardapioGeral(cls):
        lista_cardapios = []
        for cardapio in cls.listaCardapio:
            pratos_dia = []
            pratos_dia.append(cls.abrirCardapioDia(cardapio.getData()))
            lista_cardapios.append({"dia": cardapio.getData(), "refeições": pratos_dia})
        return lista_cardapios