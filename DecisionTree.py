from GameBoard import GameBoard

class Node:

    def __init__(self, move: int = None, depth: int = None):
        self.move = move
        self.score = None
        self.children = []
        self.board = GameBoard()
    def getBoard(self)->GameBoard:
    	return self.board
    def setBoard(self, board):
    	self.board = board
    """def getNextMove(self)->int:
        return self.nextMove
    def setNextMove(self, move: int = None):
        self.nextMove = move"""
    def getMove(self)->int:
    	return self.move
    def setMove(self, move: int = None):
        self.move = move
    def getChildren(self) ->list:
    	return self.children
    def getScore(self)->int:
    	return self.score
    def setScore(self, score: int = None):
        self.score = score
    def getNumChildren(self)->int:
    	return len(self.children)

class TicTacToeDecisionTree:

    def setupTree(self, root:Node, emptySpacesList):
        emptySpaces = len(emptySpacesList)
        for i in range(emptySpaces):
            nextMove = emptySpacesList[i]
            nextNode = Node(nextMove,9-(emptySpaces-1))
            root.children.append(nextNode)
            newEmptySpacesList=[]
            for j in range(emptySpaces):
            	if not i==j:
            		newEmptySpacesList.append(emptySpacesList[j])
            if not len(newEmptySpacesList)==0:
            	self.setupTree(nextNode, newEmptySpacesList)


    def __init__(self):
        self.root = Node()
        self.root.depth = 0

        emptySpaces = []
        for i in range(9):
        	emptySpaces.append(i)
        self.setupTree(self.root,emptySpaces)

#    def getRoot(self)->Node:
#    	return self.root
    def addChild(self, move: int = None):
        root.children.append(Node())

    def printTree(self,n):
        print(n.value)
       	for child in n.children:
       		self.printTree(child)




