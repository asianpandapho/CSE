import random


class Characters(object):
    def __init__(self, name, desc, health, attack):
        self.name = name
        self.desc = desc
        self.health = health
        self.attack = attack
        self.dead = False

    def take_damage(self, amt):
            self.health -= amt

    def swing(self, target):
        target.take_damage(self.attack)
        print('%s attacks %s' % (self.name, target.name))
        if target.health <= 0:
            target.dead = True
            print('%s died' % target.name)
            exit(0)

    def fight(self, enemy, Weapons):
        print('You engage in a fight with the %s' % bad.name)

        while self.health != 0:
            choice = random.choice([enemy, self])
            if choice == self:
                enemy.swing(self)
            elif choice == enemy:
                self.swing(enemy)
                print('You attacked the %s with your %s' % enemy.name, Weapons.name)


class Enemy(Characters):
    def __init__(self, name, desc, health, damage):
        super(Enemy, self).__init__(name, desc, 100, 25)
        self.health = health
        self.damage = damage


class Carni(Enemy):
    def __init__(self, name, desc, big, small):
        super(Carni, self).__init__(name, desc, 100, 25)
        self.big = big
        self.small = small


class TRex(Carni):
    def __init__(self):
        super(TRex, self).__init__("T Rex", "A T Rex that does tons of damage", True, False)


class IRex(Carni):
    def __init__(self):
        super(IRex, self).__init__('I Rex', "An I Rex that does tons of damage", True, False)


class Mega(Carni):
    def __init__(self):
        super(Mega, self).__init__('Megalodon', 'A big shark that will eat you', True, False)


class Spino(Carni):
    def __init__(self):
        super(Spino, self).__init__('Spinosaurus', 'A big Spinosaurus that does tons of damage', True, False)


class Velo(Carni):
    def __init__(self):
        super(Velo, self).__init__('Velociraptor', 'A smaller dinosaur that will claw your face', False, True)


class Diloph(Carni):
    def __init__(self):
        super(Diloph, self).__init__('Dilophosaurus', 'A smaller dinosaur that will claw your face', False, True)


class Herb(Enemy):
    def __init__(self, name, desc):
        super(Herb, self).__init__(name, desc, 200, 15)
        
        
class Tri(Herb):
    def __init__(self):
        super(Tri, self).__init__('Triceratops', 'An angry Ticeratops that will poke you with its horns')
        
        
class Brachio(Herb):
    def __init__(self):
        super(Brachio, self).__init__('Brachiosaurus', 'A big dinosaur that will whip you with its tail')
    
    
class Stego(Herb):
    def __init__(self):
        super(Stego, self).__init__('Stegosaurus', 'A dinosaur that has spikes ok its tail that do a lot of damage')


class Item(object):
    def __init__(self, name, desc, value):
        self.name = name
        self.desc = desc
        self.value = value
        self.equip = False

    def use(self):
        print("You use the %s " % self.name)

    def equip(self):
        self.equip = True
        print("You equipped a %s" % self.name)

    def sell(self):
        print("You sell the %s for %d gold" % (self.name, self.value))


class Weapons(Item):
    def __init__(self, name, desc, damage):
        super(Weapons, self).__init__(name, desc, 100)
        self.damage = damage

    def attack(self, Enemy, Weapons):
        print("You attack the %s with your %s" % Enemy.name, Weapons.name)


class Tranq(Weapons):
    def __init__(self):
        super(Tranq, self).__init__("Tranquilizer Gun", "Makes enemies drowzy and fall asleep", 10)


class Flare(Weapons):
    def __init__(self):
        super(Flare, self).__init__("Flare Gun", "Scares away smaller Dinosaurs", 5)


class Scar(Weapons):
    def __init__(self):
        super(Scar, self).__init__('FN Scar', 'A powerful assault rifle that does a lot of damage', 50)


class Tool(Item):
    def __init__(self, name, desc, uses):
        super(Tool, self).__init__(name, desc, 50)
        self.uses = uses


class Screwdriver(Tool):
    def __init__(self):
        super(Screwdriver, self).__init__("Screwdirver", "A normal screwdriver", 4)

    def unscrew(self):
        print("You use the screwdriver")


class Flashlight(Tool):
    def __init__(self):
        super(Flashlight, self).__init__("Flashlight", "A normal flashlight", 5)

    def on(self):
        print('You turn the Flashlight on')

    def off(self):
        print('You turn off the flashlight')


class Misc(Item):
    def __init__(self, name, desc, uses):
        super(Misc, self).__init__(name, desc, 50)
        self.uses = uses


class OdorAway(Misc):
    def __init__(self, spray):
        super(OdorAway, self).__init__("Odor Away", "Takes your smell away", 1)
        self.spray = spray

    def spray(self):
        print('You sprayed the Odor Away, now dinosaurs wont be able to smell you for and hour')


class Lighter(Misc):
    def __init__(self, light):
        super(Lighter, self).__init__("Lighter", "A small lighter", 1)
        self.light = light


class Net(Misc):
    def __init__(self):
        super(Net, self).__init__("Net", "A big net", 1)


class Healing(Item):
    def __init__(self, name, desc, uses):
        super(Healing, self).__init__(name, desc, 30)
        self.uses = uses


class MedKit(Healing):
    def __init__(self):
        super(MedKit, self).__init__("Med Kit", "A Med Kit that will fully heal you", 1)


class Bandage(Healing):
    def __init__(self):
        super(Bandage, self).__init__('Bandage', "A Bandage that will heal you for 10 health", 1)


you = Characters('you', 'you are yourself', 50, 50)
bad = Characters('dino', 'This is a bad guy', 45, 70)

you.fight(bad, Scar)
