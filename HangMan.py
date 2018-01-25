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
word_bank = ["YASUO", "RENGAR", "KATARINA", "GRAVES", "ZED", "AKALI", "ZOE", "FIZZ", "FIORA", "HASAGI"]
guesses = 10
alphabet = list(string.ascii_uppercase)
random_word = random.choice(word_bank)
print(random_word)
print("Lets play Hangman, you have 10 guesses, what am I thinking?")
letters_guessed = []

while guesses > 0:
    guesses -= 1
    print(guesses)
    print("These are your letters, %s" % alphabet)
    ask_for_letter = input("Name a letter")
    uppercase_guess = ask_for_letter.upper()
    letters_guessed.append(uppercase_guess)
    if uppercase_guess in alphabet:
        alphabet.remove(uppercase_guess)
    for letter in random_word:
        if uppercase_guess in random_word:
            letters_guessed.append(uppercase_guess)
            print(letters_guessed)
    if str(alphabet) in random_word is True:
        guesses + 1


    # if righ_guesses == word:
    #     print("YOU WIN XD")
    #
    #     if end == "Yes":
    #         print(answer)
    if letters_guessed == random_word:
        print(random_word)
        print("You Win XD!")

    #     if already_guessed != string.ascii_uppercase:
    #          = string.ascii_uppercase
    #

# Anou Her
