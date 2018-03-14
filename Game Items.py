class Inventory(object):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def use(self):
        print("You use the %s " % self.name)


class Weapons(Inventory):
    def __init__(self, name, desc, damage):
        super(Weapons, self).__init__(name, desc)
        self.damage = damage
        self.equip = False
        self.unequip = True


class Tranq(Weapons):
    def __init__(self):
        super(Tranq, self).__init__("Tranquilizer Gun", "Makes enemies drowzy and fall asleep", 10)


class Flare(Weapons):
    def __init__(self):
        super(Flare, self).__init__("Flare Gun", "Scares away smaller Dinosaurs", 5)


class Tool(Inventory):
    def __init__(self, name, desc, ):
        super(Tool, self).__init__(name, desc)
        self.equip = False
        self.unequip = True



