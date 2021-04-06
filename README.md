# pands-problem-sheet
This repository contains the weekly tasks for PANDS 2021. In addition to this README file I have also included comments in the code to explain the reasoning behind my code. 

Week 1 Task:
The task this week was to copy the link to the repository. I figured this out by watching the lecture multiple times and following the lab. I didn't use any external sources this week to complete the task. I did look up additional videos on youtube but found the lecture to be the best guide. 


Week 2 Task: bmi.py
The task this week was to create a simple program that calculates a user's BMI. It was difficult to find a simple solution online because most pages like stackexchange had more complex calculators. I mostly got the solution from watching the lecture and then from watching a youtube video and reading a blog as a suplemental. These sources have been included in comments in the code.

Week 3 Task: secondString.py
The task this week was to write a program that asked the user to input a string and then output every second letter in the string in reverse.
Getting an external solution for this program was a little more difficult because most stack exchange solutions used functions which we had not covered yet. So I got most of the solution from following the lecture, W3schools as well as trial and error. The example given on w3schools was return x[::-1] which slices the string and moves backwards from the end of the string. By putting x[::-2] into the program we still start at the end put work back in 2s.

Week 4 Task: 
This week the task was the write a program that asks the user to input a positive integer. The program then divides the number by 2 is it is even or multiplies it by 3 and adds 1 if it is odd.
I didn't know how to complete the task during week 4 despite trying multiple attempts with if else statements. Once we moved on to functions I went back to the task and used the lecture video, a tutorial from w3schools and a website called python central to figure out the answer. 

Week 5 Task: 
This week the task was to write a program that tells the user whether or not the day of the week is a weekend or a weekday.
There was plenty of information online on how to do this. I found a few suggestions from stackoverflow and reference it in the code.
To run the program I needed to import datetime. From there I got today's date from datetime.datetime.today().weekday(). The days of the week run from 0-6 with 5 and 6 being Saturday and Sunday. Knowing this I ran an if else statement to print a message according to whether the day was a weekday or a weekend.


Week 6 Task:
The task this week was to create a program that takes in a positive number and then outputs the square root.To do this I needed to create a function that converted the sqaure root of the input number when called. 
We were advised to look up the Newton method to solve the task. The task required a lot of outside reading. I found helpful threads on Stack overflow that explained how the Newton method worked and how to code it in python. 
The most helpful source was a medium article with a simple function used to find the square root. Once I found this article it was trial and error to find the best way to print out the answer to the number the user inputs.

Week 7 Task: 
The task this week was to read in a text file and then output the number of e's in the file. To complete the task I followed the lecture, the w3schools tutorial and also read parts of the realpython tutorial to get a better understanding of the process of read and writing files in python. Once I understood the process there was plenty of threads on stackoverflow that gave solutions to similar problems. 

To count the number of e's in the file. I first created a text file in the same folder as the program I was making. I then opened the file in read mode using open("textFile.txt", "r")
Then I used the read function to read the data in the file. After that I used a simple for loop to count +1 for every e or E in the file.
The final part prints the number of e's in the file by referencing the result of the for loop.


Week 8 Task: 
The task this week was to write a program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
To complete this task I followed the lecture and then read the realpython tutorial on matplot lib.
The task required me to import numpy and matplotlib into the program.
I then used numpy.arrange to return 4 evenly spaced values within intervals of 1.
From here I plotted the lines according to the function given. I used google to figure out how they should be plotted on matplotlib and followed a tutorial on matplotlib.org.
The next part of the program is to plot the 3 lines and style them. 
Then the x axis and y axis are plotted and the legend and title of the plot are built.
The final part is to show() the plot when the program is run and to save the plot into the files as a png image.

