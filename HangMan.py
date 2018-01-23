import random
import string
"""

A general guide for Hangman
1.Make a word bank - 10
2.Pick a random item from the list
3.Add a guess to the list on letters guessed
4.Reveal the letters that have been guessed
5.Create the win condition

"""
list1 = ["YASUO", "RENGAR", "KATARINA", "GRAVES", "ZED", "AKALI", "ZOE", "FIZZ", "FIORA", "HASAGI"]
guesses = 10
list2 = list(string.ascii_uppercase)
word = (random.choice(list1))
print(word)
print("Lets play Hangman, you have 10 guesses, what am I thinking?")
already_guessed = [" ", ]
right_guesses = [" ", ]

while guesses > 0:
    guesses -= 1
    print(guesses)
    print("These are your letters, %s" % list2)
    end = input("Do you want to guess?")
    answer = input("What do you think it is")
    ask_for_letter = input("Name a letter")
    print(end)
    if end == "no":
        print("Ok")

        if end == "Yes":
            print(answer)
        if answer == word:
            print(word)
            print("You Win! XD")

    if str(list2) in word is True:
        guesses + 1

        if list2 != string.ascii_uppercase:
            list2 = string.ascii_uppercase



# Anou Her
