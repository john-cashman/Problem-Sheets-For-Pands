#This program stores the months of the year in a Tuple
#There is another Tuple for just the summer months and this is printed out
#Author: John Cashman
#Source: https://www.w3schools.com/python/python_tuples_access.asp

months = ('January', 'February', 'March', 'April', 'May', 'June' ,'July', 'August', 'September', 'October','November','December')

summerMonths = months[4:7]

for month in summerMonths:
    print(month)