from Grammar.IDList import IDList
from main import Interpreter

# Decl symbol class
class Decl:

    def __init__(self):
        self.idList = None

    # Parses decl symbol
    def Parse(self):
        #Skips int and parses id list, then skips semicolon
        Interpreter.tokenList.skipToken()
        self.idList = IDList()
        self.idList.Parse()
        Interpreter.tokenList.skipToken()

    # Prints decl symbol
    def Print(self):
        print("int ", end="")
        self.idList.Print()
        print(";")

    # Executes decl symbol
    def Execute(self):
        self.idList.Execute()
