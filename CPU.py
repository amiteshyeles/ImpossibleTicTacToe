from Player import Player
from DecisionTree import *
from GameBoard import GameBoard
import copy
class CPU(Player):
    
    def getName(self)->str:
        return self.name

    def getSymbol(self)->str:
        return self.symbol
    def setOrder(self, o:int):
        self.playerOrder=o
    #def checkExists(self, board, symbol)->int:
    # basically if there are 2 in a row return true. symbol is the current turn.
    #this will be an optimization that I will add later.


    def getResult(self,board)-> int:
        r = board.rowWinner()
        c = board.columnWinner()
        d = board.diagonalWinner()
        result=0
        #board.display()
        #print("rcd",r,c,d)
        if not r==0:
            result=r
            #print("r")
        if not c==0:
            result=c
            #print("c")
        if not d==0:
            result=d
            #print("d")
        if result<0:
            #print("-1")
            result=-1
        if result>0:
            #print("1")
            result=1
        return result
        #Positive result means you lose and negative means


    """def fillGameEndingValues(self):
        #boards = None
        print("fillgame ending values")
        symbol = "X"
        queue = []
        queue.append(self.tree.root)
        print("this is the length of the queue", len(queue))
        while not len(queue)==0:
            currNode = queue.pop(0)
            #print("enter while loop once")
            for i in range(currNode.getNumChildren()):
                nextNode = currNode.children[i]
                board = copy.deepcopy(currNode.getBoard())
                if nextNode.depth%2==1:
                    symbol = "X"
                else:
                    symbol = "O"
                #print(nextNode.getMove())
                board.update(nextNode.getMove(),symbol)
                nextNode.setBoard(board)
                if nextNode.depth>=5:
                    #print("enter depth of 5")
                    #find out if the game is over and fill in the value
                    result = self.getResult(board)
                    #nextNode.setValue(result)
                    if (not (result==0)) or (result==0 and nextNode.depth==9):
                        nextNode.setValue(result)
                        #print("value",nextNode.getValue())
                        #print(result, nextNode.getValue())
                        #print("not a draw set value")
                    else:
                        queue.append(nextNode)
                        #print("else statement of filling game ending values")
                else:
                    queue.append(nextNode)

    """
    
    def minimax(self,board,isMaximizer,lastMove)->(int,int):
        
        gBoard = GameBoard(board)
        #gBoard.display()
        if not self.getResult(gBoard)==0:
            if isMaximizer:
                return (self.getResult(gBoard),lastMove)
            return (-self.getResult(gBoard),lastMove)
        move = -1
        score = -2
        #boardMatrix = board.getBoard()
        for i in range(9):
            if board[i//3][i%3]==" ":
                boardWithNewMove = copy.deepcopy(board)
                if isMaximizer:
                    #print("maximizer")
                    boardWithNewMove[i//3][i%3]="X"
                else:
                    #print("minimizer")
                    boardWithNewMove[i//3][i%3]="O"
            
                scoreMove = self.minimax(boardWithNewMove,not isMaximizer,i)
                scoreForTheMove = -scoreMove[0]
                #print("tuple",scoreMove,"maxScore",score,"isMaximizer",isMaximizer)
                if scoreForTheMove>score:
                    
                    score = scoreForTheMove
                    move = i
    
        if move ==-1:
            return (0,-1)
        #print("returning",score,move)
        return (score,move)
    """def getPlayedMoves(self,board)->list:
                    i = 0
                    playedX = []
                    playedO = []
                    playedMoves = []
                    while i <9:
                        s = board[i//3][i%3]
                        if s=="X":
                            playedX.append(i)
                        if s=="O":
                            playedO.append(i)
                        i+=1
                    for i in range(len(playedO)+len(playedX)):
                        if i%2==0:
                            playedMoves.append(playedX.pop(0))
                        else:
                            playedMoves.append(playedO.pop(0))
                    return playedMoves
                                """
    def getMove(self, board, turn, playedMoves)->int:
        #print("Computer GetMove")
        gBoard = GameBoard(board)
        #gBoard.display()
        scoreMove = self.minimax(board,False,0)
        return scoreMove[1]

    def __init__(self, sym:str = "O", n:str = "Computer"):
        super().__init__(sym,n)
        #self.tree = TicTacToeDecisionTree()
        #self.tree.root.setBoard(GameBoard())
        #self.fillGameEndingValues()
        #self.tree.printTree(self.tree.root)
        #self.minimax(self.tree.root, 0)

#computer = CPU()
