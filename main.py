import sys
import TokenList


class Interpreter:
    tokenList = None


def main():
    # Gets tokens from tokenizer
    inputFile = sys.argv[1]
    Interpreter.tokenList = TokenList.TokenList(inputFile)
    Interpreter.tokenList.printString()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
