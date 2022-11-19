from Grammar.Cond import Cond
from Grammar.StmtSeq import StmtSeq
from Interpreter import Interpreter
from TokenList import tokenDict


class If:

    def __init__(self):
        self.c = None
        self.ss1 = None
        self.ss2 = None

    def Parse(self):
        # Cond statement
        Interpreter.tokenList.skipToken()
        self.c = Cond()
        self.c.Parse()

        # Then statement
        Interpreter.tokenList.skipToken()
        self.ss1 = StmtSeq()
        self.ss1.Parse()
        # Checks if else statement exists or not
        if Interpreter.tokenList.getTokenID() == tokenDict["end"]:
            Interpreter.tokenList.skipToken()
            Interpreter.tokenList.skipToken()
            return

        # Else Statement
        Interpreter.tokenList.skipToken()
        self.ss2 = StmtSeq()
        self.ss2.Parse()

        # End statement
        Interpreter.tokenList.skipToken()
        Interpreter.tokenList.skipToken()

    def Print(self, indent):
        print(indent + "if ", end="")
        self.c.Print(indent)
        print(" then")
        self.ss1.Print(indent + "\t")
        if self.ss2:
            print(indent + "else")
            self.ss2.Print(indent + "\t")
        print(indent + "end;")

    def Execute(self):
        if self.c.Execute():
            self.ss1.Execute()
        elif self.ss2:  # Else statement exists
            self.ss2.Execute()


