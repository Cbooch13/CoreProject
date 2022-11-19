from Grammar.ID import ID
from TokenList import tokenDict
from Interpreter import Interpreter


# ID List symbol class
class IDList:

    def __init__(self):
        self.id = None
        self.idList = None

    def Parse(self):
        self.id = ID()
        self.id.Parse()
        if Interpreter.tokenList.getTokenID() == tokenDict[","]:
            Interpreter.tokenList.skipToken()
            self.idList = IDList()
            self.idList.Parse()

    def Print(self, indent):
        self.id.Print(indent)
        if self.idList:
            print(", ", end="")
            self.idList.Print(indent)

    def Execute(self):
        pass #TODO

    #Set the value of the id
    def setIdValues(self, init):
        # Handles if the variable needs to be initialized
        if init:
            val = Interpreter.tokenList.getDataLine()
            self.id.setIDVal(val)
        else:  # Handles if the variable has been initialized and needs to be changed
            self.id.setIDVal()


