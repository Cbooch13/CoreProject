from Interpreter import Interpreter


# ID symbol class
class ID:
    # List of existing IDs
    eIDs = []

    def __init__(self):
        self.name = ""
        self.val = None
        self.isDecl = False
        self.isInit = False

    def Parse(self):
        self.name = Interpreter.tokenList.getTokenString()
        Interpreter.tokenList.checkToken("identifier")
        Interpreter.tokenList.skipToken()

        # Returns existing ID if already exists
        for eId in self.eIDs:
            if eId.name == self.name:
                return eId

        # Adds id to eIDs
        self.eIDs.append(self)

        return self

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

        return int(self.val)

    # Gets name of id object
    def setIDVal(self, value):
        # Makes sure ID is declared
        if not self.isDecl:
            print("Error: " + self.name + " has not been declared")
            exit(-1)
        self.isInit = True
        self.val = value
