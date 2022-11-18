import sys
import TokenList
from Grammar.Program import Program
from Interpreter import Interpreter


def main():
    # Gets tokens from tokenizer
    inputFile = sys.argv[1]
    Interpreter.tokenList = TokenList.TokenList(inputFile)
    Interpreter.tokenList.printString()

    program = Program()
    program.Parse()
    program.Print("\t")
    # program.Execute()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
