import random


class Characters(object):
    def __init__(self, name, description, health, attack, block):
        self.name = name
        self.description = description
        self.dead = False
        self.health = health
        self.attack = attack
        self.enemy = False
        self.block = block

    def take_damage(self, amt):
        self.health -= amt

    def fight(self, enemy):
        print('You engage in a fight with the %s' % bad.name)
        choice = random.choice([enemy, self])
        if choice == self:
            self.attack = True
            enemy.take_damage(self.attack)
            print('You attack the %s' % enemy.name)
        elif choice == enemy:
            self.take_damage(enemy.attack)
            enemy.attack = True
        if self.attack >= enemy.health:
            enemy.dead = True
            print('%s knocked out' % enemy.name)
        if enemy.attack >= self.health:
            self.dead = True

    def defend(self, enemy):
        choice = random.choice([enemy, self])
        if choice == self:
            enemy.attack = False
            print('You blocked the attack')
        if choice == enemy:
            enemy.attack = True


you = Characters('you', 'you are yourself', 3, 1, 1)
bad = Characters('dino', 'This is a bad guy', 1, 4, 1)

print(you.defend(bad))
print(you.attack)


print(bad.attack)

you.fight(bad)
