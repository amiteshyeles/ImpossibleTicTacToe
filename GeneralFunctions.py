def getIntInput(phrase:str)->int:
    val = ""
    while type(val) is not int:
        val = input(phrase)
        try:
   	        val = int(val)
        except ValueError:
            print("\nThis is not an valid number.\n")
    return val
