# Anou Her
#

import random
number = (random.randint(1, 50))
guess = ""
print(number)

while guess != number:
    guess = input("What number am I thinking about?")

# Generate a random number between 1-50
# Get a number (input) from the user
# Compare the number to the input
# Add "Higher" or "Lower"
# Add 5 guesses
