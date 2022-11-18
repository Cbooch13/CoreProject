
from Interpreter import Interpreter
from TokenList import tokenDict


# StmtSeq symbol class
class StmtSeq:

    def __init__(self):
        self.stmt = None
        self.stmtSeq = None

    def Parse(self):
        from Grammar.Stmt import Stmt
        self.stmt = Stmt()
        self.stmt.Parse()
        # Checks if stmtSeq is over
        currToken = Interpreter.tokenList.getTokenID()
        if currToken == tokenDict["end"] or currToken == tokenDict["else"]:
            return
        self.stmtSeq = StmtSeq()
        self.stmtSeq.Parse()

    def Print(self, indent):
        self.stmt.Print(indent)
        if self.stmtSeq:
            self.stmtSeq.Print(indent)

    def Execute(self):
        self.stmt.Execute()
        if self.stmtSeq:
            self.stmtSeq.Execute()

