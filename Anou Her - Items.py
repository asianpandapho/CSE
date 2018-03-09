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


flare_gun = Weapon("Flare Gun", 90, 2)
tranquilizer = Weapon("Tranquilizer Gun", 90, 1)
print(tranquilizer.value)
tranquilizer.sell()
