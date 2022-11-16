import sys
import Tokenizer


def main():
    # Gets tokens from tokenizer
    inputFile = sys.argv[1]
    tokenizer = Tokenizer(inputFile)
    print(tokenizer.tokenList)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
