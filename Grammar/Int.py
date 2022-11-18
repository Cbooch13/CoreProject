from Interpreter import Interpreter


def isInt(num):

    try:
        int(num)
        return True

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
        return self.int


