from datetime import date
from app.models.cardapio import Cardapio
from fastapi import HTTPException

class CardapioController:
    listaCardapio = [Cardapio(idCardapio=1, data="2021-10-10"),
                     Cardapio(idCardapio=2, data="2021-10-11"),
                     Cardapio(idCardapio=3, data="2021-10-12"),
                     Cardapio(idCardapio=4, data="2021-10-13"),
                     Cardapio(idCardapio=5, data="2021-10-14")]
    id_counter = 6
    cardapio_selecionado = None

    @classmethod
    def adicionarCardapio(cls, data: date):
        novo_cardapio = Cardapio(idCardapio=cls.id_counter, data=data)
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
            if cardapio.getIdCardapio() == idCardapio:
                return cardapio
        return None
    
    # @classmethod
    # def editarCardapio(cls, idCardapio: int, data: date):
    #     cardapio = cls.getCardapio(idCardapio)
    #     if cardapio is None:
    #         return None
    #     cardapio.data = data
    #     return cardapio
    
    
    @classmethod
    def getCardapioByData(cls, data: date):
        for cardapio in cls.listaCardapio:
            if cardapio.data == data:
                return cardapio
        return None
    
    @classmethod
    def abrirCardapioDia(cls, data: date):
        # importa aqui para não dar circular import
        from app.controller.refeicaoPrato_controller import RefeicaoPratoController
        from app.controller.refeicao_controller import RefeicaoController
        
        cardapio = cls.getCardapioByData(data)
        if cardapio is None:
            return None
        
        cls.cardapio_selecionado = cardapio.getIdCardapio()
        
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
    
    @classmethod
    def getCardapioSelecionado(cls):
        return cls.cardapio_selecionado

    @classmethod
    def getRefeicaoCardapio(cls, refeicao: str, idCardapio: int):
        from app.controller.refeicao_controller import RefeicaoController
        cardapio = cls.getCardapio(idCardapio)
        for ref in RefeicaoController.getRefeicaoByCardapio(cardapio.getIdCardapio()):
            if ref.getHorario() == refeicao:
                return ref
        return None
    
    @classmethod
    def getDataCardapioSelecionado(cls):
        data = cls.getCardapio(cls.cardapio_selecionado).getData()
        return data
    
    @classmethod
    def atribuirPratoCardapio(cls, nome_prato: str, horario_refeicao: str):
        from app.controller.prato_controller import PratoController
        from app.controller.refeicao_controller import RefeicaoController
        from app.controller.refeicaoPrato_controller import RefeicaoPratoController
        
        if cls.cardapio_selecionado is None:
            return None
        cardapio = cls.getCardapio(cls.cardapio_selecionado)
        
        prato = PratoController.getPratoByNome(nome_prato)
        if prato is None:
            return None
        
        ref = cls.getRefeicaoCardapio(horario_refeicao, cardapio.getIdCardapio())
        if ref is None:
            ref = RefeicaoController.adicionarRefeicao(horario_refeicao, cardapio.getIdCardapio())
            
        if RefeicaoPratoController.isPratoInRefeicao(prato.getIdPrato(), ref.getIdRefeicao()):
            return None
        RefeicaoPratoController.adicionarRefeicaoPrato(prato.getIdPrato(), ref.getIdRefeicao())
        
        return cls.abrirCardapioDia(cls.getDataCardapioSelecionado())