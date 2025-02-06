#Write a program able to play the 
# "Guess the number" - game, where the 
# number to be guessed is randomly chosen
# between 1 and 20. This is how it should
# work when run in a terminal:

import random

def guess_the_number():
    name = input("Hello! What is your name? ")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    attempts = 0

    while True:
        guess = int(input("\nTake a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"\nGood job, {name}! You guessed my number in {attempts} guesses!")
            break


guess_the_number()

#Hello! What is your name? kbtu

#Well, kbtu, I am thinking of a number between 1 and 20.

#Take a guess: 1
#Your guess is too low.

#Take a guess: 12
#Your guess is too high.

#Take a guess: 5
#Your guess is too low.

#Take a guess: 8
#Your guess is too high.

#Take a guess: 7
#Your guess is too high.

#Take a guess: 6

#Good job, kbtu! You guessed my number in 6 guesses!