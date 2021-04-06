#This program reads in a text file and outputs the number of e's the text file contains.

#This opens the text file and reads it in.
myText = open("textFile.txt", "r")

#uses read function. Variable name set to str1. 
str1 = myText.read()

# find the number of the Es in file
e_count =  0
for letter in str1: #for loop here. For every e or E in str1 add 1 to the count.
    if( letter=='E' or letter=='e'):
        	e_count +=1
        
print('The Number of E\'s in text file :', e_count) # this prints the result. Uses backspace to allow the ' to be used.
myText.close() #closes the file


# references:
# https://realpython.com/read-write-files-python/
#  https://pythonexamples.org/python-count-number-of-characters-in-text-file/,
# https://easycodebook.com/python-text-file-program-to-count-vowels/
# https://stackoverflow.com/questions/48885930/counting-specific-characters-in-a-file-python
# https://www.w3schools.com/python/python_file_open.asp