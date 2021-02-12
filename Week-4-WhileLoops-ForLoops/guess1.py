#This gets a user to guess a number. This will promt the user to keep guessing until the get the number right
#Author: John Cashman

numberToGuess = 30

guess = int(input(" Please guess the number: "))
while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again: "))

print ("Well done! Yes the number was ", numberToGuess)