#This is a program to randomly generate a fruit
#Author: John Cashman

import random

fruits =['Apple', 'Orange', 'Banana', 'Pear']

#this bit gets a random number between 0 and length-1
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print("A random fruit:{}".format(fruit))
