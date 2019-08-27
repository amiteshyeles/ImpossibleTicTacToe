from random import randrange
from GameBoard import GameBoard
from Human import Human
from CPU import CPU
from TicTacToeErrors import *
from GeneralFunctions import *
import copy

class TicTacToe:

    def __init__(self):
        self.board = GameBoard()

    def getNumPlayers(self)->int:
	    print("Play against a friend or CPU")
	    gettingNumPlayers = True
	    while gettingNumPlayers:
	        numPlayers = getIntInput("Enter 1 for single player and 2 for 2 player: ")
	        if numPlayers<1:
	            print("\nToo few Players\n")
	        elif numPlayers>2:
	            print("\nToo many Players\n")
	        else:
	            gettingNumPlayers = False
	    return numPlayers
    def modifyTurnOrder(self,players):
        if randrange(1)==1:
            players.append(players.pop(0))
    def playGame(self) -> None:
        player1 = Human("X","Player 1")
        player2  = None
        players = [player1]

        numPlayers = self.getNumPlayers()
        if numPlayers==1:
            player2 = CPU()
            player2.setOrder(2)
        else:
        	player2 = Human("O", "Player 2")
        players.append(player2)
        self.modifyTurnOrder(players)
        turn = 1
        playedMoves = []
        while not self.board.isGameOver() and turn<=9:
            self.board.display()
            move = players[(turn-1)%2].getMove(self.board.getBoard(), turn,copy.copy(playedMoves))
            playedMoves.append(move)
            self.board.update(move,players[(turn-1)%2].getSymbol())
            turn+=1

        self.board.display()
        if not self.board.isGameOver():
            print("It's a Draw :|")
        elif self.board.rowWinner()<0 or self.board.columnWinner()<0 or self.board.diagonalWinner()<0:
            print(players[1].getName(), "wins!")
        else:
            print(players[0].getName(), "wins!")
