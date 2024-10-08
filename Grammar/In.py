from Grammar.IDList import IDList
from Interpreter import Interpreter


class In:

    def __init__(self):
        self.idList = None

    def Parse(self):
        # Parses read, idList, and semicolon
        Interpreter.tokenList.checkToken("read")
        Interpreter.tokenList.skipToken()
        self.idList = IDList()
        self.idList.Parse()
        Interpreter.tokenList.checkToken(";")
        Interpreter.tokenList.skipToken()

    def Print(self, indent):
        print(indent + "read ", end="")
        self.idList.Print(indent)
        print(";")

    def Execute(self):
        self.idList.setIdValues()
