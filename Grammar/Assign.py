from Grammar.Exp import Exp
from Grammar.ID import ID
from Interpreter import Interpreter


# Assign symbol class
class Assign:

    def __init__(self):
        self.id = None
        self.exp = None

    def Parse(self):
        # Parse id and equals sign
        self.id = ID()
        self.id = self.id.Parse()
        Interpreter.tokenList.checkToken("=")
        Interpreter.tokenList.skipToken()

        # Parse exp and semicolon
        self.exp = Exp()
        self.exp.Parse()
        Interpreter.tokenList.checkToken(";")
        Interpreter.tokenList.skipToken()

    def Print(self, indent):
        print(indent, end="")
        self.id.Print(indent)
        print(" = ", end="")
        self.exp.Print(indent)
        print(";")

    def Execute(self):
        # Set id val to exp val
        self.id.setIDVal(self.exp.Execute())


