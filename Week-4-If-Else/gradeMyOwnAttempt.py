#This program takes in a students percentage mark and prints a corresponding grade
#Author: John Cashman

score = float(input("enter your score in percentage:  "))

if score < 40:
    print(":( you Failed")
elif score >= 40:
    print("Huzzah you passed !!!")
elif score >= 50:
    print("You scored a merit 2")
elif score >= 60:
    print("You scored a Merit 1")
else:
    print("You score a distinction. Congrats! ")

#This doesn't work because anything over 40 is meeting the pass criteria