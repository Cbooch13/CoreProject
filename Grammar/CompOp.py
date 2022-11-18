from TokenList import tokenDict
from Interpreter import Interpreter


# CompOp symbol class
class CompOp:

    def __init__(self):
        self.altNo = 0
        self.compOp = None

    def Parse(self):
        # Gets alternative of compOp
        currToken = Interpreter.tokenList.getTokenID()
        if currToken == tokenDict["!="]:
            self.altNo = 1
            self.compOp = "!="
        elif currToken == tokenDict["=="]:
            self.altNo = 2
            self.compOp = "=="
        elif currToken == tokenDict["<"]:
            self.altNo = 3
            self.compOp = "<"
        elif currToken == tokenDict[">"]:
            self.altNo = 4
            self.compOp = ">"
        elif currToken == tokenDict["<="]:
            self.altNo = 5
            self.compOp = "<="
        elif currToken == tokenDict[">="]:
            self.altNo = 6
            self.compOp = ">="
        Interpreter.tokenList.skipToken()

    def Print(self, indent):
        print(" " + self.compOp + " ", end="")

    def Execute(self):
        return self.compOp
