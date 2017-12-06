# Anou Her
#

import random
number = (random.randint(0, 50))
guess = "0"
yes = "Correct"
only5guess = "5"


while int(guess) != number:
    guess = input("What number from 1- 50 am I thinking about?")
    if guess == str(number):
        print(yes)
    elif int(guess) >= number:
        print("Lower")
    elif int(guess) <= number:
        print("Higher")
    elif int(only5guess) >= int(guess):
        print("You Lose Get Rekt M8!")

# Generate a random number between 1-50
# Get a number (input) from the user
# Compare the number to the input
# Add "Higher" or "Lower"
# Add 5 guesses
