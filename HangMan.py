import random
import string
"""

A general guide for Hangman
1.Make a word bank - 10
2.Pick a random item from the list
3.Hide the word (use *)
4.Reveal the letters that have been guessed
5.Create the win condition

"""

list1 = ["Yasuo", "Death is like the wind, always by my side", "Katarina", "Graves", "One blade, one purpose",
         "Make it quick", "No cure for fools", "Sorye ge ton", "Face The Wind", "Hasagi"]
guesses = 15
letters = string.ascii_uppercase

#    ____
#   |    |
#   |    O
#   |   /|\
#   |    |
#   |   / \
#  _|_
# |   |______
# |          |
# |__________|

for item in list1:
    print(item)

while guesses >= 0:
    guesses -= 1
    print(list1[random.choice(1, 10)])


# Anou Her
