from Interpreter import Interpreter
from TokenList import tokenDict


# Exp symbol class
class Exp:

    def __init__(self):
        self.fac = None
        self.exp = None
        self.isAdding = None

    def Parse(self):
        from Grammar.Fac import Fac
        self.fac = Fac()
        self.fac.Parse()
        if Interpreter.tokenList.getTokenID() == tokenDict["+"]:  # Fac + Exp
            self.isAdding = True
            Interpreter.tokenList.skipToken()
            self.exp = Exp()
            self.exp.Parse()

        elif Interpreter.tokenList.getTokenID() == tokenDict["-"]:  # Fac - Exp
            self.isAdding = False
            Interpreter.tokenList.skipToken()
            self.exp = Exp()
            self.exp.Parse()

    def Print(self, indent):
        self.fac.Print(indent)
        if self.exp:
            if self.isAdding:
                print(" + ", end="")
            else:
                print(" - ", end="")
            self.exp.Print(indent)

    def Execute(self):
        pass
