#This function reads in a number from a file that already exists and tests to see if it works
#Author: John Cashman

filename = "count.txt"
def readNumber():
    with open(filename) as f: #here filename is count.txt
        number = int(f.read()) # converts the number read back as an integer
        return number #reads back the number contained in count.txt


num = readNumber() #num is the function defined above
print (num) 