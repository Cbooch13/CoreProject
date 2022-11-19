from Grammar.IDList import IDList
from Interpreter import Interpreter


class Out:

    def __init__(self):
        self.idList = None

    def Parse(self):
        # Parses write, idList, and semicolon
        Interpreter.tokenList.checkToken("write")
        Interpreter.tokenList.skipToken()
        self.idList = IDList()
        self.idList.Parse()
        Interpreter.tokenList.checkToken(";")
        Interpreter.tokenList.skipToken()

    def Print(self, indent):
        print(indent + "write ", end="")
        self.idList.Print(indent)
        print(";")

    def Execute(self):
        self.idList.writeIDValues()
