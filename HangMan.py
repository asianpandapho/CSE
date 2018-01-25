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
word_bank = ["YASUO", "RENGAR", "KATARINA", "GRAVES", "ZED", "AKALI", "UDYR", "FIZZ", "FIORA", "HASAGI"]
guesses = 10
alphabet = list(string.ascii_uppercase)
random_word = random.choice(word_bank)
correct = list(random_word)
print(random_word)
print("Lets play Hangman, you have 10 guesses, what am I thinking?")
letters_guessed = []


while guesses > 0:
    output = []
    for letter in random_word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print(output)
    guesses -= 1
    if output == correct:
        print("You Win")
        exit(0)
    print("These are your letters, %s" % alphabet)
    ask_for_letter = input("Name a letter")
    uppercase_guess = ask_for_letter.upper()
    letters_guessed.append(uppercase_guess)
    if uppercase_guess in alphabet:
        alphabet.remove(uppercase_guess)
    if guesses == 0:
        print("You Lose the word was %s" % random_word)

# Anou Her
