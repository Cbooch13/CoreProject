from Grammar.Cond import Cond
from Grammar.StmtSeq import StmtSeq
from Stmt import Stmt
from main import Interpreter


class Loop(Stmt):

    def __init__(self):
        self.c = None
        self.ss = None

    def Print(self):
        print("while")
        self.c.Print()
        print("loop")
        self.ss.Print()
        print("end;");

    def Execute(self):
        while self.c.evalCond():
            self.ss.Execute()

        return

    def Parse(self):
        # Cond statement
        Interpreter.tokenList.skipToken()
        self.c = Cond()
        self.c.Parse()

        # Loop statement
        Interpreter.tokenList.skipToken()
        self.ss = StmtSeq()
        self.ss.Parse()

        # End statement
        Interpreter.tokenList.skipToken()
        Interpreter.tokenList.skipToken()
        return
