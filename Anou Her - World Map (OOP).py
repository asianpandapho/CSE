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


# Initialize Rooms
airplane = Room("Airplane Landing Area\n",
                "You are in the Airplane Landing Area, you can only go North\n"
                " to go to the gate.", "GATE", "You can't go there", "You can't go there", "You can't go there\n",
                "You can't go there", "You can't go there", "You can't go there", "You can't go there",)

gate = Room("Gate Entrance\n",
            'You are at the entrance of the park, '
            'You are a electrician and you came to do a checkup\n'
            'You have on you a screwdriver and a flashlight\n'
            'there are paths East, West, Northeast, and Northwest, and South\n',
            'You can\'t go there', 'airplane', 'lab', 'visit', 'velo', 'tri', 'You can\'t go there\n',
            'You can\'t go there')

lab = Room("Laboratory\n",
           'You go to the Laboratory and look at how the genetically modify dinosaurs\n'
           'There is a tranquilizer gun on the desk and there is a flare gun on the desk,\n'
           'the tranquilizer has 5 bullets in it while the flare has 3, however you can only take 1\n'
           ' conveniently there is a button with the marking DANGER! on it, and there is a path Northeast\n',
           'You can\'t go there', 'You can\'t go there', 'tri', 'You can\'t go there', 'You can\'t go there\n',
           'You can\'t go there', 'You can\'t go there', 'You can\'t go there')

visit = Room('Visitor Center\n',
             'You are at the Visitor Center here Visitors can buy items,\n'
             'like Odor Away, a net, and bug spray, and a custom Jurrasic Park lighter\n'
             ' there is a path Northwest,\n',
             'You can\'t go there', 'You can\'t go there', 'You can\'t go there', 'You can\'t go there\n',
             'You can\'t go there', 'You can\'t go there', 'velo', 'You can\'t go there')

velo = Room("Velociraptor Cage\n",
            'You arrive at Velociraptor Valley where you see 4 Velociraptors running around and jumping.\n'
            'They have one huge claw on both of their feet, and they are scared of flares\n.'
            ' There are paths Northeast, North, and West\n',
            'spino', 'You can\'t go there', 'tri', 'You can\'t go there', 'diloph', 'You can\'t go there\n',
            'You can\'t go there', 'You can\'t go there')

tri = Room('Triceratops Cage\n',
           'You arrive at Triceratops Track , there is a Triceratops munching on some leaves,\n'
           'it looks pretty friendly however you should not get close to it,\n'
           '(I feel you can ride it though\n)'
           ' there are paths Northwest, East, and North\n',
           'brachio', 'You can\'t go there', 'You can\'t go there', 'velo', 'You can\'t go there\n'
           'mega', 'You can\'t go there', 'You can\'t go there', 'You can\'t go there')

brachio = Room('Brachiosaurus Cage\n',
               'You arrive at Brachiosaurus Bridge, you see huge dinosaurs walking around and eating from\n'
               'massive trees, there are paths West, East, and North\n',
               'stego', 'You can\'t go there', 'mega', 'spino', 'You can\'t go there', 'You can\'t go there\n',
               'You can\'t go there', 'You can\'t go there')

spino = Room('Spinosaurus Cage\n',
             'You arrive at Spinosaurus Station and see a huge Spinosaurus, it look very hungry,\n'
             'you don\'t want to mess with it, however 2 trang bullets will make it unconscious\n'
             ' there are paths East, North, and West\n',
             't_rex', 'You can\'t go there', 'brachio', 'diloph', 'You can\'t go there', 'You can\'t go there\n'
             'You can\'t go there', 'You can\'t go there', 'You can\'t go there')

diloph = Room('Dilophasaurus Cage\n',
              'You arrive at Dilophosaurus Dungeon and see 4 Dilophosaurus fighting,\n'
              'and they look very hungry, they can all be scared off by a flare if you shoot it properly\n'
              'there are paths West and Northwest\n',
              'You can\'t go there', 'You can\'t go there', 'spino', 'You can\'t go there', 'You can\'t go there\n',
              '', 'You can\'t go there', 'You can\'t go there',)

mega = Room('Megalodon Cage\n',
            'You arrive at Megalodon Waters and see 1 huge shark in the water,\n'
            'it looks like it can jump out at you at any second,\n'
            'but it remains calm for now just don\t drop blood into the water\n'
            'there are paths East and Northeast\n',
            'You can\'t go there', 'You can\'t go there', 'You can\'t go there', 'brachio', 'stego\n',
            'You can\'t go there', 'You can\'t go there', 'You can\'t go there')

t_rex = Room('Tyrannosaurus Cage\n',
             'You arrive at the Tyrannosaurus Jungle, there you see the king of dinosaurs,\n'
             'it can be tranquilized with 3 tranq bullets,\n'
             ' there are paths North and West\n',
             'I_REX', 'You can\'t go there', 'stego', 'You can\'t go there', 'You can\'t go there\n',
             'You can\'t go there', 'You can\'t go there', 'You can\'t go there')

stego = Room('Stegosaurus Cage\n',
             'You arrive at Stegosaurus Springs, you see the Stegosaurus drinking water,\n'
             'you might need to befriend it later\n'
             ' there are paths North and East\n',
             'PTER', 'You can\'t go there', 'You can\'t go there', 't_rex', 'You can\'t go there\n',
             'You can\'t go there', 'You can\'t go there', 'You can\'t go there')

i_rex = Room('Indominous Rex Cage\n',
             'You arrive at Indominous Rex Swamp, you cant see anything but trees,\n'
             ' however you feel a presence someone told you that the I Rex can be tranquilized by 5 darts\n'
             ', there are paths Northwest and West\n',
             'You can\'t go there', 'You can\'t go there', 'pter', 'You can\'t go there', 'You can\'t go there\n',
             'copter', 'You can\'t go there', 'You can\'t go there')

pter = Room('PTERODACTYL CAGE\n'
            'You arrive at Pterodactyl City, you see them fly in the sky,\n'
            'it looks like they can just swoop down an grab you off the ground, a flare can scare them off\n'
            ' there are paths Northeast and East\n',
            'You can\'t go there', 'You can\'t go there', 'You can\'t go there', "i_rex", 'copter\n',
            'You can\'t go there', 'You can\'t go there', 'You can\'t go there', 'You can\'t go there',)

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
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    if command in long_directions:
        index = long_directions.index(command)
        command = directions[index]
    if command in directions:
        try:
            name_of_node = current_node.move(directions)
            current_node = name_of_node
        except KeyError:
            print('You cannot go this way')
    else:
        print('command not Recognized')
    if current_node == copter:
        print('You arrive at the Helipad, you get onto the helicopter and leave the Island. GOOD JOB!')
        exit(0)
