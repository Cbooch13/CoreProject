from Grammar.IDList import IDList
from Interpreter import Interpreter


# Decl symbol class
class Decl:

    def __init__(self):
        self.idList = None

    # Parses decl symbol
    def Parse(self):
        # Skips int and parses id list, then skips semicolon
        Interpreter.tokenList.checkToken("int")
        Interpreter.tokenList.skipToken()
        self.idList = IDList()
        self.idList.Parse()
        Interpreter.tokenList.checkToken(";")
        Interpreter.tokenList.skipToken()

    # Prints decl symbol
    def Print(self, indent):
        print(indent + "int ", end="")
        self.idList.Print(indent)
        print(";")

    # Executes decl symbol
    def Execute(self):
        self.idList.declareIDs()

