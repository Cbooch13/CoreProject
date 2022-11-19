import sys
import TokenList
from Grammar.Program import Program
from Interpreter import Interpreter


def main():
    # Gets tokens from tokenizer
    inputFile = sys.argv[1]
    inputData = sys.argv[2]
    Interpreter.tokenList = TokenList.TokenList(inputFile, inputData)

    program = Program()
    program.Parse()
    program.Print("")
    program.Execute()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
