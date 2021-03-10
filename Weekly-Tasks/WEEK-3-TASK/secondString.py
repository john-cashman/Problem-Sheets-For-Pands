#This is the task for week 3. 
#This program asks the user to input a string and then outputs every second letter in reverse order
#Author: John Cashman
#Source: https://www.w3schools.com/python/python_howto_reverse_string.asp

#This part takes the input string
MyString = input('enter a string: ')

#This part reverses the string backwards and slices every second character
Reverse = MyString[::-2]

#This part prints the result.
print('{}'.format(Reverse))


