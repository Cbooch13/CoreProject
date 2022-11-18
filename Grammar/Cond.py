from Grammar.Comp import Comp
from TokenList import tokenDict
from Interpreter import Interpreter


# Cond symbol class
class Cond:
    def __init__(self):
        self.comp = None
        self.altNo = 0
        self.cond1 = None
        self.cond2 = None

    def Parse(self):
        # Checks what alternative is being used and parses it accordingly
        currToken = Interpreter.tokenList.getTokenID()
        if currToken == tokenDict["("]:  # Comp
            self.altNo = 1
            self.comp = Comp()
            self.comp.Parse()
        elif currToken == tokenDict["!"]:  # !Cond
            self.altNo = 2
            Interpreter.tokenList.skipToken()
            self.cond1 = Cond()
            self.cond1.Parse()
        else:
            Interpreter.tokenList.skipToken()
            self.cond1 = Cond()
            self.cond1.Parse()
            currToken = Interpreter.tokenList.getTokenID()
            if currToken == tokenDict["&&"]:  # [Cond && Cond]
                self.altNo = 3
            else:  # [Cond || Cond]
                self.altNo = 4
            Interpreter.tokenList.skipToken()
            self.cond2 = Cond()
            self.cond2.Parse()
            Interpreter.tokenList.skipToken()

    def Print(self, indent):
        if self.altNo == 1:  # Comp
            self.comp.Print(indent)
        elif self.altNo == 2:  # !Cond
            print("!", end="")
            self.cond1.Print(indent)
        elif self.altNo == 3:  # [Cond && Cond]
            print("[", end="")
            self.cond1.Print(indent)
            print(" && ", end="")
            self.cond2.Print(indent)
            print("]", end="")
        elif self.altNo == 4:  # [Cond || Cond]
            print("[", end="")
            self.cond1.Print(indent)
            print(" || ", end="")
            self.cond2.Print(indent)
            print("]", end="")

    def Execute(self):
        if self.altNo == 1:  # Comp
            self.comp.Execute()
        elif self.altNo == 2:  # !Cond
            pass
        elif self.altNo == 3:  # [Cond && Cond]
            pass
        elif self.altNo == 4:  # [Cond || Cond]
            pass
