class spaceFullError(Exception):
	
	def __init__(self, pieceOnSpace : str="", msg = None):
		if msg is None:
			msg = "This space is full already. There is an %s", pieceOnSpace
		super(spaceFullError,self).__init__(msg)


class notOnBoardError(Exception):
	
	def __init__(self,msg = None):
		if msg is None:
			msg = "This input is not on the board!"
		super(notOnBoardError, self).__init__(msg)

class sameSymbolError(Exception):

    def __init__(self,msg = None):
        if msg is None:
            msg = "Both players chose the same symbol!"
        super(sameSymbolError,self).__init__(msg)
