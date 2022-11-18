from Grammar.Exp import Exp
from Grammar.ID import ID
from Grammar.Int import Int
from TokenList import tokenDict
from Interpreter import Interpreter


class Op:

    def __init__(self):
        self.altNo = 0
        self.altOp = None

    def Parse(self):
        currToken = Interpreter.tokenList.getTokenID()
        if currToken == tokenDict["("]:  # (Exp)
            Interpreter.tokenList.skipToken()
            self.altNo = 1
            self.altOp = Exp()
            self.altOp.Parse()
            Interpreter.tokenList.skipToken()
        elif currToken == tokenDict["integer"]:  # Int
            self.altNo = 2
            self.altOp = Int()
            self.altOp.Parse()
        else:  # ID
            self.altNo = 3
            self.altOp = ID()
            self.altOp.Parse()

    def Print(self, indent):
        if self.altNo == 1:
            print("(", end="")
            self.altOp.Print(indent)
            print(")", end="")
        else:
            self.altOp.Print(indent)

    def Execute(self):
        pass
