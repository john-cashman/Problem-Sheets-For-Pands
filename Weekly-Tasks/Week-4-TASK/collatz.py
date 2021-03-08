#This program takes in a positive integer and outputs values according to the following calculation
#If the integer is even, the program will divide the integer by 2 but if it is odd the program will multiply it by 3 and add 1
#The program will end when the value is 1
#Author: John Cashman
#Sources: https://www.pythoncentral.io/using-python-to-check-for-odd-or-even-numbers/, https://www.w3schools.com/python/python_conditions.asp
#, 

number = int(input("please enter a positive number: "))

#This is the function. It is called later in the program
def getNumber(number):
    if number % 2 == 0: # This checks if the number is divisible by 2 (even)
        return number//2 # if the number is even it is divided by 2
    else:
        return((number*3)+1) # if the number is not divisible by 2 it is odd. And therefore it is multiplied by 3 and 1 is added.


if number >0: # This states as long as the number is positive and not 1 then the program outputs the calculation from the function.
    while number != 1:
        print(number)
        number = getNumber(number) #number is the number entered in the above function     

else: 
    print("please enter a positive number: ") # if the user does not enter a positive number they will get this prompt

