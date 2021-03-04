#This function reads in a number from a file that already exists and tests to see if it works


filename = "count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number
num = readNumber()
print (num)