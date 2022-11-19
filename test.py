import os

print("**************************************SUCCESSES**************************************\n-\n-\n-")

print("--------------------------------------------")
print("Running badBinarySearch.txt with NUM = 10...")
os.system("python3 main.py data/badBinarySearch.txt data/inputData.txt")
print("--------------------------------------------\n-\n-\n-")

print("--------------------------------------------")
print("Running fibonacci.txt with NUM = 100...")
os.system("python3 main.py data/fibonacci.txt data/fibonacciData.txt")
print("--------------------------------------------\n-\n-\n-")

print("--------------------------------------------")
print("Running testData3.txt with ABC = 10, D = 9...")
os.system("python3 main.py data/testData3.txt data/inputData.txt")
print("--------------------------------------------\n-\n-\n-")

print("--------------------------------------------")
print("Running testData1.txt with ABC = -10, D = -10...")
os.system("python3 main.py data/testData1.txt data/negativeData.txt")
print("--------------------------------------------\n-\n-\n-")

print("**************************************ERRORS**************************************\n-\n-\n-")

print("--------------------------------------------")
print("Running testData4.txt with ABC = 10, D = 9...")
print("Expecting an error concerning T not being initialized")
os.system("python3 main.py data/testData4.txt data/inputData.txt")
print("--------------------------------------------\n-\n-\n-")

print("--------------------------------------------")
print("Running testData2.txt with X4 = 10...")
print("Expecting an error concerning PIE not being declared")
os.system("python3 main.py data/testData2.txt data/inputData.txt")
print("--------------------------------------------\n-\n-\n-")

print("--------------------------------------------")
print("Running fibonacci.txt with NUM = None...")
print("Expecting an error concerning the inability to read the data file")
os.system("python3 main.py data/fibonacci.txt data/blankInputData.txt")
print("--------------------------------------------\n-\n-\n-")

print("--------------------------------------------")
print("Running badInputData.txt with NUM = 10...")
print("Expecting an error concerning the missing keyword, aka incorrect grammar")
os.system("python3 main.py data/badInputData.txt data/inputData.txt")
print("--------------------------------------------\n-\n-\n-")
