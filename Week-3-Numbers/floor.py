#This program takes in a float and outputs an integer rounded down.
#John Cashman

import math

#This part asks for a float number to be entered
numberTofloor = float(input('Enter a float number: '))

#This rounds the number down
flooredNumber = math.floor(numberTofloor)

#This prints the result
print('{} floored is {}'.format(numberTofloor,flooredNumber))