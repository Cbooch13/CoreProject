from Grammar.DeclSeq import DeclSeq
from Grammar.StmtSeq import StmtSeq
from main import Interpreter


#Program symbol class
class Program:

    def __init__(self):
        self.declSeq = None
        self.stmtSeq = None

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

    def Print(self):


    def Execute(self):
