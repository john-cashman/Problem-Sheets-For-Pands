#This program is an improvement of guess1.py where it tells the user if they are guessing to high or low
#Author: John Cashman

numberToGuess = 30

guess = int(input(" Please guess the number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("Too Low") 
    else: 
        print(" too high")   
    guess = int(input("Please guess again: "))

print ("Well done! Yes the number was ", numberToGuess)