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
list1 = ["Yasuo", "Rengar", "Katarina", "Graves", "Zed", "Akali", "Zoe", "Fizz", "Fiora", "Hasagi"]
guesses = 10
letters = string.ascii_uppercase
word = (random.choice(list1))
print(word)
end = "What do you think it is?"
print("Lets play Hangman, you have 10 guesses, what am I thinking?")

while guesses > 0:
    guesses -= 1
    print(guesses)
    start = input("These are your letters, %s" % letters)
    print(start)
    if end == word:
        print(word)
        print("You Win! XD")
        if letters != string.ascii_uppercase:
            letters = string.ascii_uppercase



# Anou Her
