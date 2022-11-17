from Grammar.DeclSeq import DeclSeq
from Grammar.StmtSeq import StmtSeq
from main import Interpreter


#Program symbol class
class Program:

    def __init__(self):
        self.declSeq = None
        self.stmtSeq = None

    # Parses program
    def Parse(self):
        #Program keyword and declaration sequence
        Interpreter.tokenList.skipToken()
        self.declSeq = DeclSeq()
        self.declSeq.Parse()

        #Begin keyword and statement sequence
        Interpreter.tokenList.skipToken()
        self.stmtSeq = StmtSeq()
        self.stmtSeq.Parse()

        #End keyword
        Interpreter.tokenList.skipToken()

    # Prints program
    def Print(self):
        print("program")
        self.declSeq.Print()
        print("begin")
        self.stmtSeq.Print()
        print(" end")

    # Executes Program
    def Execute(self):
        self.declSeq.Execute()
        self.stmtSeq.Execute()
