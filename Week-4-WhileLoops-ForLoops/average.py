#This program keeps reading numbers until the user enters a 0
#Author: John Cashman

numbers = []

#Gets the user to enter a number
number = int(input("enter number(0 to quit):"))

#checks if the number entered is zero
while number != 0:
    numbers.append(number)
    #The program then reads the next number and checks if it is 0
    number = int(input(" enter another number (0 to quit): "))

for value in numbers:
    print (value)

#This gets the average of the numbers entered and puts it into a float
average = float(sum(numbers)) / len(numbers)
print ("The average is {}".format(average))