#This function takes in a number and overwrites a file with that number.
#Author: John Cashman

filename = "count.txt"
def writeNumber(number):
    with open(filename, "wt") as f:
        f.write(str(number)) # takes the number and converts to a string so we can write it to a file

writeNumber(3)