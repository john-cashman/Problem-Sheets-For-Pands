#This program takes two numbers and subtracts the first number from the second number
#Author: John Cashman


#Here the user is asked to input the first and second number. 
#int ensures that the result is recorded as an integer
x= int (input("Enter first number: "))
y= int (input("Enter second number: "))

#This is the code I wrote without checking the answer
z = x - y
print(" When you take {} from {} you get {}".format(y,x,z))

#The lab answer is below
print("{} minus {} is {}".format(x,y,z))
