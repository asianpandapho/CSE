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

    def swing(self, target):
        target.take_damage(self.attack)
        print('%s attacks %s' % (self.name, target.name))
        if target.health <= 0:
            target.dead = True
            print('%s died' % target.name)
            exit(0)

    # Transfer to controller
    def fight(self, enemy):
        print('You engage in a fight with the %s' % bad.name)

        while self.health != 0:
            choice = random.choice([enemy, self])
            if choice == self:
                enemy.swing(self)
            elif choice == enemy:
                self.swing(enemy)

    def defend(self, enemy):
        choice = random.choice([enemy, self])
        if choice == self:
            enemy.attack = False
            print('You blocked the attack')
        if choice == enemy:
            enemy.attack = True
            print('The %s blocked your attack' % enemy.name)


you = Characters('you', 'you are yourself', 3, 1, 1)
bad = Characters('dino', 'This is a bad guy', 3, 1, 1)

you.fight(bad)
