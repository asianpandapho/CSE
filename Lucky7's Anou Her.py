import random


rigged_stuff = 7
money = 15


while money > 0:
    dice1 = (random.randint(1, 6))
    dice2 = (random.randint(1, 6))
    print(dice1)
    print(dice2)

    roll = (dice1 + dice2)

    if roll == rigged_stuff:
        print(money + 4)
    elif roll != 7:
        print(money - 1)



# Anou Her
