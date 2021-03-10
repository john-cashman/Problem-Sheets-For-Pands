#This program outputs whether or not today is a weekday
#Author: John Cashman
# Source: https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python


import datetime #imports dates into the program

today = datetime.datetime.today().weekday() # today is today's day within the week. Week runs from 0-6

if today <5: #if today is less the day 5 (day 5 and 6 are Saturday and Sunday)
    print("It is a weekday :( ") 
else: # if today is 5 or 6 then it is a weekend
    print (" It is the weekend wohooo! ")

    
