# Caleb Bucci
# Core tokenizer program

import sys

# Constants
KEYWORDS = {"program": 1, "begin": 2, "end": 3, "int": 4, "if": 5, "then": 6,
            "else": 7, "while": 8, "loop": 9, "read": 10, "write": 11}
SYMBOLS = {";": 12, ",": 13, "[": 16, "]": 17, "(": 20,
           ")": 21, "+": 22, "-": 23, "*": 24}
SPECIAL = {"=": 14, "!": 15, "&&": 18, "||": 19, "!=": 25,
           "==": 26, "<": 27, ">": 28, "<=": 29, ">=": 30}

UNSIGNED_INT = 31
IDENTIFIER = 32
EOF = 33
WHITESPACE = [" ", "\n", "\t", "\r"]


# Tokenizer class
class Tokenizer:

    def __init__(self, inputFile):
        self.f = open(inputFile, "r")
        self.token = ""
        self.line = ""
        self.start = 0
        self.tokenID = 0

    # Returns the first valid token, start at index start up to either the next token or whitespace, start < len(line)
    # The starting character cannot be whitespace or empty
    def getToken(self):

        # Initialize starting token
        self.token = self.line[self.start]
        idx = self.start + 1

        # Handles symbols with no special exceptions in SYMBOL dict
        if self.token in SYMBOLS:
            self.tokenID = SYMBOLS[self.token]

        # Handles multi-char or special tokens in SPECIAL dict
        elif self.token in SPECIAL or (idx < len(self.line) and self.token + self.line[idx] in SPECIAL):
            if idx < len(self.line) and self.token + self.line[idx] in SPECIAL:
                self.token += self.line[idx]
            self.tokenID = SPECIAL[self.token]

        # Handles integers
        elif self.token.isdigit():
            self.token = captureString(self.line, self.start)
            self.intVal()
            self.tokenID = UNSIGNED_INT

        # Handles keywords
        elif self.token.islower():
            self.token = captureString(self.line, self.start)
            if self.token not in KEYWORDS:
                handleBadToken(self.token)
            self.tokenID = KEYWORDS[self.token]

        # Handles identifiers
        elif self.token.isupper():
            self.token = captureString(self.line, self.start)
            self.idName()
            self.tokenID = IDENTIFIER

        # Bad token
        else:
            self.token = captureString(self.line, self.start)
            handleBadToken(self.token)

    # Changes start to after current token
    def skipToken(self):

        self.start += len(self.token)
        self.start += skipWhitespace(self.line, self.start)

    # Returns value of int or returns an error if not an int
    def intVal(self):
        retInt = -1
        try:
            retInt = int(self.token)

        except ValueError:
            handleBadToken(self.token)

        return retInt

    # Returns id name or an error if invalid id
    def idName(self):
        for char in self.token:
            if not (char.isupper() or char.isdigit()):
                handleBadToken(self.token)
        return self.token


# Returns length of first whitespace in line starting at start and ending at first non whitespace character in line
def skipWhitespace(line, start):
    idx = start
    while idx < len(line) and line[idx] in WHITESPACE:
        idx += 1

    return idx - start


# Returns the first substring of line starting at start and ending at the first whitespace or symbol
def captureString(line, start):
    retString = ""
    idx = start
    while idx < len(line) and line[idx] not in WHITESPACE and line[idx] not in SYMBOLS and line[idx] not in SPECIAL:
        retString += line[idx]
        idx += 1
    return retString


def handleBadToken(token):
    print("Error: '" + token + "' is an invalid token")
    exit(1)


# Generates array of tokens from inputFile
def genTokenList(inputFile):
    tokenList = []
    # Creates tokenizer, opens file and reads from it for the tokenizer, file must be a valid file to read from
    tokenizer = Tokenizer(inputFile)

    tokenizer.line = tokenizer.f.readline()
    while tokenizer.line:
        tokenizer.start = 0
        tokenizer.start += skipWhitespace(tokenizer.line, tokenizer.start)
        while tokenizer.start < len(tokenizer.line):
            tokenizer.getToken()
            tokenList.append(tokenizer.tokenID)

            tokenizer.skipToken()

        tokenizer.line = tokenizer.f.readline()
    tokenList.append(EOF)

    # Closes file
    tokenizer.f.close()

    return tokenList
