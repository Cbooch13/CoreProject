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
            Interpreter.tokenList.checkToken("[")
            Interpreter.tokenList.skipToken()
            self.cond1 = Cond()
            self.cond1.Parse()
            currToken = Interpreter.tokenList.getTokenID()
            if currToken == tokenDict["&&"]:  # [Cond && Cond]
                self.altNo = 3
            elif currToken == tokenDict["||"]:  # [Cond || Cond]
                self.altNo = 4
            else:  # Error
                print("Expected a conditional operator but got " + tokenDict[currToken])
                exit(-1)

            # Parses conditional operator, cond2, and brackets
            Interpreter.tokenList.skipToken()
            self.cond2 = Cond()
            self.cond2.Parse()
            Interpreter.tokenList.checkToken("]")
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
            return self.comp.Execute()
        elif self.altNo == 2:  # !Cond
            return not self.cond1.Execute()
        elif self.altNo == 3:  # [Cond && Cond]
            return self.cond1.Execute() and self.cond2.Execute()
        elif self.altNo == 4:  # [Cond || Cond]
            return self.cond1.Execute() or self.cond2.Execute()
        else:
            print("Error executing condition")
            exit(-1)

