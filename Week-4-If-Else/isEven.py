#This program takes in a number and then tells the user if it is even or odd
#Author: John Cashman

#This part takes in the number
number = int(input("enter an integer: "))

#This part says if the number is divided by two and there is nothing left over then it is an even number
#The else part says if there are numbers left over then it is an odd number.
if(number % 2) == 0:
    print("{} is an even number".format(number))
else:
    print("{} is an odd number".format(number))
