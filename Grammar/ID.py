from Interpreter import Interpreter


# ID symbol class
class ID:
    # List of declared IDs
    eIDs = []

    def __init__(self):
        self.name = ""
        self.val = None
        self.isDecl = False
        self.isInit = False

    def Parse(self):
        self.name = Interpreter.tokenList.getTokenString()
        Interpreter.tokenList.skipToken()

        # Adds id to eIDs
        if self not in self.eIDs:
            self.eIDs.append(self)
            self.isDecl = True

    def Print(self, indent):
        print(self.name, end="")

    def Execute(self):
        pass  # TODO

    # Gets value of id object
    def getIDVal(self):
        # Makes sure ID is initialized
        if not self.isInit:
            print("Error: " + self.name + " has not been initialized")
            exit(-1)

        return self.val

    # Gets name of id object
    def setIDVal(self, value):
        # Makes sure ID is declared
        if not self.isDecl:
            print("Error: " + self.name + " has not been declared")
            exit(-1)
        self.isInit = True
        self.val = value
