# This calculates a person's BMI
#Author: John Cashman

#This part gets the user's weight
weight = int(input('Enter your weight'))
print('you weigh {} kilos'.format(weight))

#This part gets the user's height
height = int(input('please enter your height:'))
print(' you are {} cms tall'.format(height))

#This part calculates the BMI and tells the user
bmi = height * weight
print('This means that your BMI is {}'.format(bmi))