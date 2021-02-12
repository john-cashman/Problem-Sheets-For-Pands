#This program generates a random number between 1 and 100 and it tells the user if they are guessing to high or low
#Author: John Cashman
#Reference: https://codereview.stackexchange.com/questions/100539/guess-a-random-number-between-1-and-100
# I mixed the import random part from an answer on stackexchange with the rest of the code given in the lab and it works


import random
numberToGuess = random.randint(1,100)

guess = int(input(" Please guess the number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("Too Low") 
    else: 
        print(" too high")   
    guess = int(input("Please guess again: "))

print ("Well done! Yes the number was ", numberToGuess)