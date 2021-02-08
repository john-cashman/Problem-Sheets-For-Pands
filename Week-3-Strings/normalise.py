#This program reads in a string and gets rid of any spaces
#It also converts letters to lower case
#it also outputs the length of the original string and the normalised one too
#Author: John Cashman

#This part takes in the string and the second bit normalises it
rawString = input('please enter a string: ')
normalisedString = rawString.strip().lower()


#This generates the length of the raw string as well as the normalised string
lengthOfRawString = len(rawString)
lenthOfNormalised = len(normalisedString)

#This part prints the results
print('The string normalised is: {}'.format(normalisedString))
print(' we reduced the input string from {} to {} characters'.format(lengthOfRawString,lenthOfNormalised))

#Note the output is not striping correctly
