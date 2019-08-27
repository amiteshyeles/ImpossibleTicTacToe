from Player import Player
from GeneralFunctions import *
from TicTacToeErrors import *

class Human(Player):
    
    def __init__(self, sym:str = "X", n:str="Player 1"):
        super().__init__(sym,n)


    def getMove(self, board, turn,playedMoves)->int:

        print("Choose a Spot to play!")
        gettingInput = True
        while gettingInput:
            try:
                row = getIntInput("Enter a row number (0 to 2): ")
                col = getIntInput("Enter a column number (0 to 2): ")
                if row<0 or row>2 or col<0 or col>2:
                    raise notOnBoardError()
                if not board[row][col]==" ":
                    raise spaceFullError()
                gettingInput = False
            except notOnBoardError:
                print("\nInput is not on the Board\n")
            except spaceFullError:
                print("\nThis space has already been taken\n")

        return row*3+col
