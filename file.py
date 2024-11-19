import sys


#Task 2
#The point of this program is to read a file (input.txt) that is intended to have two float values
#in each line. With this, it is supposed to sup the pairs of these float values from each line, and
#then print the sum. The input is a string that represents the name of the file. The output is intended
#to print the sum of each pair of these float values in the file. An error message is intended to be
#printed if the line doesn't have 2 numbers. So, if there is a letter, word, or anything that is not
#two numbers, then an error message will show.

sys.argv = ['file.py', 'input.txt']
if len(sys.argv) != 2:
    print("Error: Please provide the name of the file.")
    sys.exit(1)
filename = sys.argv[1]
try:
    infile = open(filename, 'r')
    lineNumber = 1
    for i in infile:
        i = i.strip()
        val = i.split()
        if len(val) != 2:
            print("Error in line " + str(lineNumber) + ": ")
        else:
            try:
                number1 = float(val[0])
                number2 = float(val[1])
                print("Line " + str(lineNumber) + " sum " + ": " + str(number1 + number2))
            except ValueError:
                print("Error in line " + str(lineNumber) + ":")
        lineNumber += 1
    infile.close()
except FileNotFoundError:
    print("Error: File '" + filename + "' not found.")