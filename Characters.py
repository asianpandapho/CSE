class Characters(object):
    def __init__(self, name, description, health, attack):
        self.name = name
        self.description = description
        self.dead = False
        self.health = health
        self.attack = attack
        self.enemy = False

    def take_damage(self, amt):
        self.health -= amt
        self.dead = True
        print("You knocked out")

    def fight(self, enemy):
        print('You engage in a fight with the %s' % bad.name)
        enemy.take_damage(self.attack)
        if self.attack >= enemy.health:
            enemy.dead = True
        if enemy.attack >= self.health:
            self.dead = True


you = Characters('you', 'you are yourself', 45, 10)
bad = Characters('dino', 'This is a bad guy', 10, 1)

print(you.name)
print(you.description)
print(you.health)
print(you.attack)

print(bad.name)
print(bad.description)
print(bad.health)
print(bad.attack)

you.fight(bad)
