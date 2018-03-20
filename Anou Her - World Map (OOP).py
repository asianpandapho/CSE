import random


class Room(object):
    def __init__(self, name, description, north, south, west, east, northeast, northwest, southeast, southwest):
        self.name = name
        self.description = description
        self.n = north
        self.s = south
        self.w = west
        self.e = east
        self.ne = northeast
        self.nw = northwest
        self.se = southeast
        self.sw = southwest

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


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

    def fight(self, enemy):
        print('You engage in a fight with the %s' % enemy.name)

        while self.health != 0:
            choice = random.choice([enemy, self])
            if choice == self:
                enemy.swing(self)
            elif choice == enemy:
                self.swing(enemy)


class Enemy(Characters):
    def __init__(self, name, desc, health, damage):
        super(Enemy, self).__init__(name, desc, 100, 25, 1)
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


class Inventory(object):
    def __init__(self, equip, unequip):
        self.opened = False
        self.equip = equip
        self.unequip = unequip
        self.closed = True


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


you = Characters('you', 'you are yourself', 50, 50, 1)


# Initialize Rooms
airplane = Room("Airplane Landing Area\n",
                "You are in the Airplane Landing Area, you can only go North\n"
                " to go to the gate.", "gate", "You can't go there", "You can't go there", "You can't go there\n",
                "You can't go there", "You can't go there", "You can't go there", "You can't go there",)

gate = Room("Gate Entrance\n",
            'You are at the entrance of the park, '
            'You are a electrician and you came to do a checkup\n'
            'You have on you a screwdriver and a flashlight\n'
            'there are paths East, West, Northeast, and Northwest, and South\n',
            None, 'airplane', 'lab', 'visit', 'velo', 'tri', None, None)

lab = Room("Laboratory\n",
           'You go to the Laboratory and look at how the genetically modify dinosaurs\n'
           'There is a tranquilizer gun on the desk and there is a flare gun on the desk,\n'
           'the tranquilizer has 5 bullets in it while the flare has 3, however you can only take 1\n'
           ' conveniently there is a button with the marking DANGER! on it, and there is a path Northeast\n',
           None, None,  None, None, 'tri', None, None, None)

visit = Room('Visitor Center\n',
             'You are at the Visitor Center here Visitors can buy items,\n'
             'like Odor Away, a net, and a custom Jurrasic Park lighter\n'
             ' there is a path Northwest,\n',
             None, None, None, None, None, 'velo', None, None)

velo = Room("Velociraptor Cage\n",
            'You arrive at Velociraptor Valley where you see 4 Velociraptors running around and jumping.\n'
            'They have one huge claw on both of their feet, and they are scared of flares\n.'
            ' There are paths Northeast, North, and West\n',
            'spino', None, 'tri', None, 'diloph', None, None, None)

vel = Characters

tri = Room('Triceratops Cage\n',
           'You arrive at Triceratops Track , there is a Triceratops munching on some leaves,\n'
           'it looks pretty friendly however you should not get close to it,\n'
           '(I feel you can ride it though)\nnn'
           ''
           ' there are paths Northwest, East, and North\n', 'brachio', None, None, 'velo', None, 'mega', None, None)

brachio = Room('Brachiosaurus Cage\n',
               'You arrive at Brachiosaurus Bridge, you see huge dinosaurs walking around and eating from\n'
               'massive trees, there are paths West, East, and North\n',
               'stego', None, 'mega', 'spino', None, None, None, None)

spino = Room('Spinosaurus Cage\n',
             'You arrive at Spinosaurus Station and see a huge Spinosaurus, it look very hungry,\n'
             'you don\'t want to mess with it, however 2 trang bullets will make it unconscious\n'
             ' there are paths East, North, and West\n',
             't_rex', None, 'brachio', 'diloph', None, None, None, None)

diloph = Room('Dilophasaurus Cage\n',
              'You arrive at Dilophosaurus Dungeon and see 4 Dilophosaurus fighting,\n'
              'and they look very hungry, they can all be scared off by a flare if you shoot it properly\n'
              'there are paths West and Northwest\n',
              None, None, 'spino', None, None, 't_rex', None, None,)

mega = Room('Megalodon Cage\n',
            'You arrive at Megalodon Waters and see 1 huge shark in the water,\n'
            'it looks like it can jump out at you at any second,\n'
            'but it remains calm for now just don\'t drop blood into the water\n'
            'there are paths East and Northeast\n',
            None, None, None, 'brachio', 'stego', None, None, None)

t_rex = Room('Tyrannosaurus Cage\n',
             'You arrive at the Tyrannosaurus Jungle, there you see the king of dinosaurs,\n'
             'it can be tranquilized with 3 tranq bullets,\n'
             ' there are paths North and West\n',
             'i_rex', None, 'stego', None, None, None, None, None)

stego = Room('Stegosaurus Cage\n',
             'You arrive at Stegosaurus Springs, you see the Stegosaurus drinking water,\n'
             'you might need to befriend it later\n'
             ' there are paths North and East\n',
             'pter', None, None, 't_rex', None, None, None, None)

i_rex = Room('Indominous Rex Cage\n',
             'You arrive at Indominous Rex Swamp, you cant see anything but trees,\n'
             ' however you feel a presence someone told you that the I Rex can be tranquilized by 5 darts\n'
             ', there are paths Northwest and West\n',
             None, None, 'pter', None, None, 'copter', None, None)

pter = Room('Pterodactyl Cage\n',
            'You arrive at Pterodactyl City, you see them fly in the sky,\n'
            'it looks like they can just swoop down an grab you off the ground, a flare can scare them off\n'
            ' there are paths Northeast and East\n',
            None, None, None, "i_rex", 'copter', None, None, None)

copter = Room('HELIPAD\n',
              'You arrive at the Helipad, you get onto the helicopter and leave the Island.\n',
              None, None, None, None, None, None, None, None,)

current_node = airplane
directions = ['n', 'e', 's', 'w', 'ne', 'nw', 'se', 'sw']
long_directions = ['north', 'east', 'south', 'west', 'northeast', 'northwest', 'southeast', 'southwest']

inventory = ['screwdriver', 'flashlight', ]
item1 = "tranquilizer"
item2 = "flare gun"
item3 = 'odor away'
item4 = 'lighter'

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    if command in long_directions:
        index = long_directions.index(command)
        command = directions[index]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print('You can\'t go this way')
    else:
        print('command not Recognized')
    if current_node == copter:
        print('You arrive at the Helipad, you get onto the helicopter and leave the Island. GOOD JOB!')
        exit(0)
