from Grammar.Cond import Cond
from Grammar.StmtSeq import StmtSeq
from Interpreter import Interpreter


# Loop symbol class
class Loop:

    def __init__(self):
        self.c = None
        self.ss = None

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

    def Print(self, indent):
        print(indent + "while ", end="")
        self.c.Print(indent + "\t")
        print(" loop")
        self.ss.Print(indent + "\t")
        print(indent + "end;")

    def Execute(self):
        while self.c.Execute():
            self.ss.Execute()
