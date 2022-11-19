from Grammar.CompOp import CompOp
from Grammar.Op import Op
from Interpreter import Interpreter


# Comp symbol class
from TokenList import tokenDict


class Comp:

    def __init__(self):
        self.op1 = None
        self.compOp = None
        self.op2 = None

    def Parse(self):
        # Skips parenthesis and parses symbols
        Interpreter.tokenList.skipToken()
        self.op1 = Op()
        self.op1.Parse()
        self.compOp = CompOp()
        self.compOp.Parse()
        self.op2 = Op()
        self.op2.Parse()
        Interpreter.tokenList.skipToken()

    def Print(self, indent):
        print("(", end="")
        self.op1.Print(indent)
        self.compOp.Print(indent)
        self.op2.Print(indent)
        print(")", end="")

    def Execute(self):
        # Gets values of ops and compOp
        op1 = self.op1.Execute()
        compVal = self.compOp.Execute()
        op2 = self.op2.Execute()
        retVal = None

        # Calculates comp and returns value
        if compVal == "!=":
            retVal = op1 != op2
        elif compVal == "==":
            retVal = op1 == op2
        elif compVal == "<":
            retVal = op1 < op2
        elif compVal == ">":
            retVal = op1 > op2
        elif compVal == "<=":
            retVal = op1 <= op2
        elif compVal == ">=":
            retVal = op1 >= op2
        else:  # Error

            print("Error executing compare")
            self.Print("")
            exit(-1)
        return retVal


