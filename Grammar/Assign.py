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
        self.id.Parse()
        Interpreter.tokenList.skipToken()

        # Parse exp and semicolon
        self.exp = Exp()
        self.exp.Parse()
        Interpreter.tokenList.skipToken()

    def Print(self, indent):
        print(indent, end="")
        self.id.Print(indent)
        print(" = ", end="")
        self.exp.Print(indent)
        print(";")

    def Execute(self):
        pass
        # TODO
