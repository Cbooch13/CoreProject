from Grammar.DeclSeq import DeclSeq
from Grammar.StmtSeq import StmtSeq
from Interpreter import Interpreter


# Program symbol class
class Program:

    def __init__(self):
        self.declSeq = None
        self.stmtSeq = None

    # Parses program
    def Parse(self):
        # Program keyword and declaration sequence
        Interpreter.tokenList.skipToken()
        self.declSeq = DeclSeq()
        self.declSeq.Parse()

        # Begin keyword and statement sequence
        Interpreter.tokenList.skipToken()
        self.stmtSeq = StmtSeq()
        self.stmtSeq.Parse()

        # End keyword
        Interpreter.tokenList.skipToken()

    # Prints program
    def Print(self, indent):
        print(indent + "program")
        self.declSeq.Print(indent + "\t")
        print(indent + "begin")
        self.stmtSeq.Print(indent + "\t")
        print(indent + "end")

    # Executes Program
    def Execute(self):
        self.declSeq.Execute()
        self.stmtSeq.Execute()
