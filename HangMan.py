import random
import string
"""

A general guide for Hangman
1.Make a word bank - 10
2.Pick a random item from the list
3.Add a user input to the list on letters guessed
4.Reveal the letters that have been guessed
5.Create the win condition

"""
list1 = ["YASUO", "RENGAR", "KATARINA", "GRAVES", "ZED", "AKALI", "ZOE", "FIZZ", "FIORA", "HASAGI"]
guesses = 10
list2 = list(string.ascii_uppercase)
word = (random.choice(list1))
print(word)
print("Lets play Hangman, you have 10 guesses, what am I thinking?")
letters_guessed = []
right_guesses = []

while guesses > 0:
    guesses -= 1
    print(guesses)
    print("These are your letters, %s" % list2)
    ask_for_letter = input("Name a letter")
    high = ask_for_letter.upper()
    letters_guessed.append(high)
    if high in list2:
        list2.remove(high)
    if list2 in word:
        right_guesses.append(high)
        print(right_guesses)
        if str(list2) in word is True:
            guesses + 1


    # if righ_guesses == word:
    #     print("YOU WIN XD")
    #
    #     if end == "Yes":
    #         print(answer)
        if right_guesses == word:
            print(word)
            print("You Win! XD")

    #     if already_guessed != string.ascii_uppercase:
    #          = string.ascii_uppercase
    #

# Anou Her
