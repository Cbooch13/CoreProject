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
        self.id = self.id.Parse()
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
        pass

    # Set the value of the id
    def setIdValues(self):
        self.id.setIDVal(Interpreter.tokenList.getDataLine())
        if self.idList:
            self.idList.setIdValues()

    # Writes values out to standard output
    def writeIDValues(self):
        self.id.Print("")
        print(" = ", end="")
        print(self.id.getIDVal())
        if self.idList:
            self.idList.writeIDValues()
