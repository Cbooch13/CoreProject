from abc import ABC, abstractmethod

from Grammar.Assign import Assign
from Grammar.In import In
from Grammar.Loop import Loop
from Grammar.Out import Out
from Grammar.If import If
from main import Interpreter


# Statement class
class Stmt(ABC):

    def __init__(self):
        self.st = None

    @abstractmethod
    def Print(self):
        self.st.Print()

    @abstractmethod
    def Execute(self):
        self.st.Execute()

    @abstractmethod
    def Parse(self):
        self.parseSt()

    def parseSt(self):

        # Determines alternative
        currToken = Interpreter.tokenList.getTokenID()
        if currToken == 7:  # Assign
            self.st = Assign()
        elif currToken == 8:  # If
            self.st = If()
        elif currToken == 9:  # Loop
            self.st = Loop()
        elif currToken == 10:  # In
            self.st = In()
        elif currToken == 11:  # Out
            self.st = Out()
        else:  # Other
            print("Unknown Alternative of Statement")

        # Parse statement
        self.st.Parse()
