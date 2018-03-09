class Item(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def sell(self):
        print("You sell the %s for %d gold" % (self.name, self.value))


class Weapon(Item):
    def __init__(self, name, value, dmg):
        super(Weapon, self).__init__(name, value)
        self.damage = dmg


axe = Weapon("Wiebe's Axe", 9001, 10000)
print(axe.value)