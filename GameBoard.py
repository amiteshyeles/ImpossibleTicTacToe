from TicTacToeErrors import *
from GeneralFunctions import *
from Player import *
from CPU import *

class GameBoard:
    USER_CHARACTER = "X"
    COMPUTER_CHARACTER = "O"

    def __init__(self):
        #self.board = [[" "]*3]*3
        self.board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    
    def setSymbols(s1:str, s2:str):
        if s2!=s1:
            USER_CHARACTER = s1
            COMPUTER_CHARACTER = s2
        else:
            raise sameSymbolError()
    def getBoard(self)->list:
        return self.board
    def diagonalWinner(self)->int:
        #output is 1 for backslash diagonal and 2 for forward slash diagonal. - output is computer win
        #output is 0 if no winner
        if self.board[0][0]==self.board[1][1]==self.board[2][2]:
            val = self.board[1][1]
            if val==self.USER_CHARACTER:
                return 1
            elif val==self.COMPUTER_CHARACTER:
                return -1
        if self.board[2][0]==self.board[1][1]==self.board[0][2]:
            val = self.board[1][1]
            if val==self.USER_CHARACTER:
                return 2
            elif val==self.COMPUTER_CHARACTER:
                return -2
        return 0

    def columnWinner(self)->int:
        #output is column number +1 of win. if output is - of the colNumber that means computer won.
        #if out is 0 then no columnWinner
        for c in range(len(self.board)):
            if self.board[0][c]==self.board[1][c]==self.board[2][c]:
                if self.board[0][c] == self.USER_CHARACTER:
                    return (c+1)
                elif self.board[0][c]==self.COMPUTER_CHARACTER:
                    return -1*(c+1)
        return 0


    def rowWinner(self)->int:
        #output is row number +1 of win. if output is - of the rownumber that means computer won.
        #if out is 0 then no rowWinner
        for r in range(len(self.board)):
            if self.board[r][0]==self.board[r][1]==self.board[r][2]:
                if self.board[r][0] == self.USER_CHARACTER:
                    return (r+1)
                elif self.board[r][0]==self.COMPUTER_CHARACTER:
                    return -1*(r+1)
        return 0

    def isGameOver(self)->bool:
        r = self.rowWinner()
        c = self.columnWinner()
        d = self.diagonalWinner()
    
        if r==0 and d==0 and c==0:
            return False
        return True

    def update(self, move: int, symbol:str):
        self.board[move//len(self.board)][move%len(self.board)]=symbol
    
    def display(self):
        for r in range(len(self.board)*2-1):
            if r%2==0:
                print(" ", end = "")
                for c in range(len(self.board[0])):
                    if c+1==len(self.board):
                        print(self.board[int((r+1)/2)][c])
                    else:
                        print(self.board[int((r+1)/2)][c], end = "|")
            else:
                print("-------")
