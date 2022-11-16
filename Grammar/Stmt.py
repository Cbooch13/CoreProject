from abc import ABC, abstractmethod
from Tokenizer import tokenList


# Statement class
class Stmt(ABC):

    def __init__(self):
        self.st = None

    @abstractmethod
    def Print(self):
        pass

    @abstractmethod
    def Execute(self):
        pass

    @abstractmethod
    def Parse(self):
        pass

    def parseSt(self):

        # Determines alternative
        currToken = t.getToken()
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


class While(Stmt):

    def __init__(self):
        self.c = None
        self.ss = None

    def Print(self):
        print("while")
        self.c.Print()
        print("loop")
        self.ss.Print()
        print("end;");

    def Execute(self):
        while self.c.evalCond():
            self.ss.Execute()

        return

    def Parse(self):
        # Cond statement
        t.skipToken()
        self.c = Cond()
        self.c.Parse()

        # Loop statement
        t.skipToken()
        self.ss = SS()
        self.ss.Parse()

        # End statement
        t.skipToken()
        t.skipToken()
        return


class If(Stmt):

    def __init__(self):
        self.c = None
        self.ss1 = None
        self.ss2 = None

    def Print(self):
        print("if")
        self.c.Print()
        print("then")
        self.ss1.Print()
        if self.ss2:
            print("else")
            self.ss2.Print()
        print("end;")
        return

    def Execute(self):
        if self.c.evalCond():
            self.ss1.Execute()
            return

        # Else statement exists
        if self.ss2:
            self.ss2.Execute()
        return

    def Parse(self):
        # Cond statement
        t.skipToken()
        self.c = Cond()
        self.c.Parse()

        # Then statement
        t.skipToken()
        self.ss1 = SS()
        self.ss1.Parse()
        tokenNo = t.getToken()
        if tokenNo == "end":
            t.skipToken()
            t.skipToken()
            return

        # Else Statement
        t.skipToken()
        self.ss2 = SS()
        self.ss2.Parse()
        tokenNo = t.getToken()

        # End statement
        t.skipToken()
        t.skipToken()
        return
