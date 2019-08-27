from abc import ABC, abstractmethod

class Player(ABC):
    
    def __init__(self,sym:str, n:str):
        self.symbol = sym
        self.name=n

    def getName(self)->str:
        if self.name == "":
            return self.symbol
        return self.name
        
    def getSymbol(self) ->str:
        return self.symbol

    @abstractmethod
    def getMove(self, board, turn,playedMoves)->int:
        #should return 3*row+col
        raise NotImplementedError("You need to implement the getMove method!")
