from Grammar.Op import Op
from TokenList import tokenDict
from Interpreter import Interpreter


# Fac symbol class
class Fac:

    def __init__(self):
        self.op = None
        self.fac = None

    def Parse(self):
        self.op = Op()
        self.op.Parse()
        if Interpreter.tokenList.getTokenID() == tokenDict["*"]:
            Interpreter.tokenList.skipToken()
            self.fac = Fac()
            self.fac.Parse()

    def Print(self, indent):
        self.op.Print(indent)
        if self.fac:
            print(" * ", end="")
            self.fac.Print(indent)

    def Execute(self):
        # Executes op and returns it if fac is Null
        leftOp = self.op.Execute()
        if not self.fac:
            return leftOp

        # Executes op * fac
        rightFac = self.fac.Execute()
        return leftOp * rightFac

