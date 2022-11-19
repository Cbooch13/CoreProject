from Interpreter import Interpreter


def isValidInt(num):

    try:
        temp = int(num)
        return temp >= 0

    except ValueError:
        return False


class Int:

    def __init__(self):
        self.int = ""

    def Parse(self):
        self.int = Interpreter.tokenList.getTokenString()
        Interpreter.tokenList.skipToken()

    def Print(self, indent):
        print(self.int, end="")

    def Execute(self):
        return int(self.int)


