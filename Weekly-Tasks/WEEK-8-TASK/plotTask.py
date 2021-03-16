#This program displays the plot for the function f(x)=x,g(x)=x2, h(x)=x3 in the range [0,4]
#Author: John Cashman

#Imports numpy and matplotlib in order to make the plot
import numpy as np
import matplotlib.pyplot as plt

#Here the range for the x axis is 0 - 4 and this happens in 1's.
x = np.arange(0.0, 4.0, 1.0)

#How the lines are to be plotted according to the equation.
y1 = x #f(x)=x
y2 = x**2 #g(x)=x2  x to the power of 2
y3 = x**3 #h(x)=x3

#this part plots y1,y2 and y3 and then styles them.
plt.plot(y1, color='green', linestyle='dotted', linewidth = 3, marker='o', markerfacecolor='red', markersize=12, label='f')
plt.plot(y2, color='blue', linestyle='dotted', linewidth = 3, marker='o', markerfacecolor='yellow', markersize=12, label='g')
plt.plot(y3, color='purple', linestyle='dotted', linewidth = 3, marker='o', markerfacecolor='orange', markersize=12, label='h')

#plots the two axis. X axis goes accross and y axis goes up.
plt.xlabel( 'x-axis' )
plt.ylabel('y-axis')

#Title of the plot
plt.title('f(x)=x, g(x)=x2 and h(x)=x3')

#Places a legend in the plot.
plt.legend()

#Shows the plot
plt.show()

#saves the plot into the same folder as the program. 
plt.savefig('plot.png')

#References: https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html
# https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# https://www.w3schools.com/python/matplotlib_pyplot.asp
#https://realpython.com/python-matplotlib-guide/
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html