#This program takes in a students percentage mark and prints a corresponding grade
#Author: John Cashman

#Takes in the percentage
score = float(input("enter your score in percentage:  "))

#
if score <0 or score >100: # This part is the initial if statement having score there twice is important. I got an error initially for not having it here a second time.
    print("please enter a number between 0 and 100") #This makes sure user puts in a valid number
elif score < 40: # a number under 40 will be a fail
    print(" Fail ")
elif score < 50: # a number between 40 and 49 will be a pass
    print(" pass ")
elif score < 60: # a number between 50 and 59 will be a merit 1
    print(" Merit 1 ")
elif score < 70:
    print(" Merit 2 ")
else: # and anything above 69 is a distinction
    print(" Distinction ")

