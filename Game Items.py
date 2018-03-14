
class Characters(object):
    def __init__(self, name, description, health, attack):
        self.name = name
        self.description = description
        self.dead = False
        self.health = health
        self.attack = attack
        self.enemy = False


class Item(object):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.equip = False

    def use(self):
        print("You use the %s " % self.name)

    def equip(self):
        self.equip = True
        print("You equipped a %s" % self.name)


class Weapons(Item):
    def __init__(self, name, desc, damage):
        super(Weapons, self).__init__(name, desc)
        self.damage = damage


class Tranq(Weapons):
    def __init__(self):
        super(Tranq, self).__init__("Tranquilizer Gun", "Makes enemies drowzy and fall asleep", 10)


class Flare(Weapons):
    def __init__(self):
        super(Flare, self).__init__("Flare Gun", "Scares away smaller Dinosaurs", 5)


class Tool(Item):
    def __init__(self, name, desc, uses):
        super(Tool, self).__init__(name, desc)
        self.uses = uses


class Screwdriver(Tool):
    def __init__(self):
        super(Screwdriver, self).__init__("Screwdirver", "A normal screwdriver", 4)


class Flashlight(Tool):
    def __init__(self):
        super(Flashlight, self).__init__("Flashlight", "A normal flashlight", 5)


class Misc(Item):
    def __init__(self, name, desc, uses):
        super(Misc, self).__init__(name, desc)
        self.uses = uses


class OdorAway(Misc):
    def __init__(self, spray):
        super(OdorAway, self).__init__("Odor Away", "Takes your smell away", 1)
        self.spray = spray


class Lighter(Misc):
    def __init__(self, light):
        super(Lighter, self).__init__("Lighter", "A small lighter", 1)
        self.light = light
