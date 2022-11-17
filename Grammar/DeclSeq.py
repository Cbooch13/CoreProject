import TokenList
from Grammar.Decl import Decl
from main import Interpreter
from TokenList import tokenDict


#Decl seq symbol class
class DeclSeq:

    def __init__(self):
        self.decl = None
        self.declSeq = None

    # Parses decl seq
    def Parse(self):
        self.decl = Decl()
        self.decl.Parse()
        #Checks if declSeq is over
        if Interpreter.tokenList.getTokenID() == TokenList.tokenDict["begin"]:
            return

        #Parses second declSeq
        self.declSeq = DeclSeq()
        self.declSeq.Parse()


    # Prints decl seq
    def Print(self):
        self.decl.Print()
        if self.declSeq:
            self.declSeq.Print()


    # Executes decl seq
    def Execute(self):
        self.decl.Execute()
        if self.declSeq:
            self.declSeq.Execute()

