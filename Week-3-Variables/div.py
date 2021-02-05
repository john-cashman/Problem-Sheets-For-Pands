#This program takes in two numbers and divides the first number by the the second number
#it then gives the remainder
#Author: John Cashman


#This part takes in the two numbers
x= int(input("Enter first number: "))
y= int(input("Enter second number: "))

#This is the division part
answer = int(x/y)

#This is the modulo part that gives the remainder
remainder = x%y


#This part prints out the results of the numbers divided
print("{} divided by {} is {} with remainder {}".format(x,y,answer,remainder))