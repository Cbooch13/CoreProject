from Interpreter import Interpreter


# ID symbol class
class ID:
    # List of initialized IDs
    initIDs = []

    def __init__(self):
        self.name = ""
        self.val = None
        self.isDecl = False
        self.isInit = False

    def Parse(self):
        self.name = Interpreter.tokenList.getTokenString()
        Interpreter.tokenList.skipToken()

    def Print(self, indent):
        print(self.name, end="")

    def Execute(self):
        pass
