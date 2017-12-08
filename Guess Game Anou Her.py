# Anou Her
#

import random
number = (random.randint(0, 50))
guess = "0"
yes = "Correct"
guesses = 0


while int(guess) != number and int(guesses) < 5:
    guess = input("What number from 1- 50 am I thinking about?")
    if int(guess) == number:
        print(yes)
    elif int(guess) >= number:
        print("Lower")
        guesses += 1
    elif int(guess) <= number:
        print("Higher")
        guesses += 1
if guesses >= 5:
    print("GET REKT M8!")


# Generate a random number between 1-50
# Get a number (input) from the user
# Compare the number to the input
# Add "Higher" or "Lower"
# Add 5 guesses
