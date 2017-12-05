# Anou Her
#

import random
number = (random.randint(1, 50))
guess = ""
print(number)

while guess != number:
    guess = input("What number from 1- 50 am I thinking about?")
    print(number == str(number))


def higher_lower(higherorlower):
    if guess == number:
        print(True)
    if guess >= str(number):
        return "Lower"
    if guess <= number:
        return "Higher"

# Generate a random number between 1-50
# Get a number (input) from the user
# Compare the number to the input
# Add "Higher" or "Lower"
# Add 5 guesses



