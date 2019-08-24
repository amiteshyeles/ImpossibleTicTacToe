from Player import Player
class CPU(Player):

    def __init__(self, sym:str = "O"):
        super().__init__(sym,"Computer")

    def getName(self)->str:
        return self.name

    def getSymbol(self)->str:
        return self.symbol

    def getMove(self, board)->int:
        pass