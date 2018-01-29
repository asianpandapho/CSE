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
word_bank = ["aatrox", "ahri", "akali", "alistar", "amumu", "anivia", "annie", "ashe", "aurelionSol" "azir", "bard",
        "blitzcrank", "brand", "braum", "caitlyn", "camille", "cassiopeia", "chogath", "corki", "darius", "diana",
        "drmundo", "draven", "ekko", "elise", "evelynn", "ezreal", "fiddlesticks", "fiora", "fizz", "galio",
        "gangplank", "garen", "gnar", "gragas", "graves", "hecarim", "heimerdinger", "illaoi", "irelia", "ivern",
        "janna", "jarvaniv", "jax", "jayce", "jinx", "kalista", "karma", "karthus", "kassadin", "katarina", "kayle",
        "kayne", "kennen", "khazix", "kindred", "kled", "kogmaw", "leblanc", "leesin", "leona", "lissandra", "lucian",
        "lulu", "lux", "malphite", "malzahar", "maokai", "masteryi", "missfortune", "mordekaiser", "morgana", "nami",
        "nasus", "nautilus", "nidalee", "nocturne", "nunu", "olaf", "orianna", "ornn", "pantheon", "poppy", "quinn",
        "rakan", "rammus", "reksai", "renekton", "rengar", "riven", "rumble", "ryze", "sejuani", "shaco", "shen",
        "shyvana", "singed", "sion", "sivir", "skarner", "sona", "soraka", "swain", "syndra", "tahmkench", "taliyah",
        "talon", "taric", "teemo", "thresh", "tristana", "trundle", "tryndamere", "twistedfate", "twitch", "udyr",
        "urgot", "varus", "vayne", "veigar", "velkoz", "vi", "viktor", "vladimir", "volibear", "warwick", "wukong",
        "xayah", "yasuo", "yorick", "zac", "zed", "ziggs", "zilean", "zoe", "zyra"]
guesses = 10
alphabet = list(string.ascii_lowercase)
random_word = random.choice(word_bank)
correct = list(random_word)
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
        print("You Win Good Job XD!")
        exit(0)
    print("These are your letters you can guess :), %s" % alphabet)
    ask_for_letter = input("Name a letter")
    lowercase_guess = ask_for_letter.lower()
    letters_guessed.append(lowercase_guess)
    if lowercase_guess in alphabet:
        alphabet.remove(lowercase_guess)
    if guesses == 0:
        print("You Lose The Word Was %s" % random_word)

# Anou Her
