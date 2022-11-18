from Grammar.Assign import Assign
from Grammar.In import In
from Grammar.Loop import Loop
from Grammar.Out import Out
from Grammar.If import If
from Interpreter import Interpreter


# Statement class
from TokenList import tokenDict


class Stmt:

    def __init__(self):
        self.st = None

    def Print(self, indent):
        self.st.Print(indent)

    def Execute(self):
        self.st.Execute()

    def Parse(self):
        # Determines alternative
        currToken = Interpreter.tokenList.getTokenID()
        if currToken == tokenDict["identifier"]:  # Assign
            self.st = Assign()
        elif currToken == tokenDict["if"]:  # If
            self.st = If()
        elif currToken == tokenDict["while"]:  # Loop
            self.st = Loop()
        elif currToken == tokenDict["read"]:  # In
            self.st = In()
        elif currToken == tokenDict["write"]:  # Out
            self.st = Out()

        # Parse statement
        self.st.Parse()

