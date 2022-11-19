import Tokenizer

tokenDict = {
    "program": 1, "begin": 2, "end": 3, "int": 4, "if": 5, "then": 6, "else": 7, "while": 8,
    "loop": 9, "read": 10, "write": 11, ";": 12, ",": 13, "=": 14, "!": 15, "[": 16, "]": 17,
    "&&": 18, "||": 19, "(": 20, ")": 21, "+": 22, "-": 23, "*": 24, "!=": 25, "==": 26,
    "<": 27, ">": 28, "<=": 29, ">=": 30, "integer": 31, "identifier": 32, "EOF": 33
}


# Class is given a token list and allows manipulation of tokens, tokenList has multiple dimensions, ex: [["A", 32]]
class TokenList:

    def __init__(self, inputFile, inputData):
        self.tokenizer = Tokenizer.Tokenizer(inputFile)
        self.data = open(inputData, "r")
        self.tokenList = self.tokenizer.tokenList
        self.tokenIdx = 0
        self.currToken = self

    # Returns tokenID
    def getTokenID(self):
        return self.tokenList[self.tokenIdx][1]

    # Returns tokenString
    def getTokenString(self):
        return self.tokenList[self.tokenIdx][0]

    # Skips to next token in list
    def skipToken(self):
        self.tokenIdx += 1

    # Returns id name or an error if invalid id
    def idName(self):
        for char in self.getTokenString():
            if not (char.isupper() or char.isdigit()):
                Tokenizer.handleBadToken(self.getTokenString())
        return self.getTokenString()

    # Returns value of int or returns an error if not an int
    def intVal(self):
        retInt = -1
        try:
            retInt = int(self.getTokenString())

        except ValueError:
            Tokenizer.handleBadToken(self.getTokenString())

        return retInt

    # Reads from input data and returns int
    def getDataLine(self):
        line = self.data.readline().strip()
        if line:
            return int(line)
        else:
            print("Error reading from input data")
            exit(-1)

    # Prints list of token ids
    def printID(self):
        print("[", end="")
        for i in range(len(self.tokenList)):
            print(self.tokenList[i][1], end="")
            if i + 1 != len(self.tokenList):
                print(",", end=" ")

        print("]")

    # Prints list of token strings
    def printString(self):
        print("[", end="")
        for i in range(len(self.tokenList)):
            print("'" + self.tokenList[i][0] + "'", end="")
            if i + 1 != len(self.tokenList):
                print(",", end=" ")

        print("]")

    # Prints list of token ids and strings
    def printAll(self):
        print(self.tokenList)
