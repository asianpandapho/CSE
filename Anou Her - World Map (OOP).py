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
        print('You engage in a fight with the %s' % bad.name)

        while self.health != 0:
            choice = random.choice([enemy, self])
            if choice == self:
                enemy.swing(self)
            elif choice == enemy:
                self.swing(enemy)


class Inventory(object):
    def __init__(self, equip, unequip):
        self.opened = False
        self.equip = equip
        self.unequip = unequip
        self.closed = True


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
             'like Odor Away, a net, and bug spray, and a custom Jurrasic Park lighter\n'
             ' there is a path Northwest,\n',
             None, None, None, None, None, None, 'velo', None)

velo = Room("Velociraptor Cage\n",
            'You arrive at Velociraptor Valley where you see 4 Velociraptors running around and jumping.\n'
            'They have one huge claw on both of their feet, and they are scared of flares\n.'
            ' There are paths Northeast, North, and West\n',
            'spino', None, 'tri', None, 'diloph', None, None, None)

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

    you = Characters('you', 'you are yourself', 3, 1, 1)
    bad = Characters('dino', 'This is a bad guy', 3, 1, 1)
