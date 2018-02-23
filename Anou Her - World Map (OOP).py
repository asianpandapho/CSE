class Room(object):
    def __init__ (self, name, description, north, south, west, east, northeast, northwest, southeast, southwest):
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

    def move(self, directions):
        global current_node
        current_node = globals()[getattr(self, directions)]


# Initialize Rooms
AIRPLANE = Room("AIRPLANE LANDING AREA\n",
                "You are in the airplane landing area, you can only go North\n"
                " to go to the gate.", "GATE", "You can't go there", "You can't go there", "You can't go there\n",
                "You can't go there", "You can't go there", "You can't go there", "You can't go there",)

GATE = Room("GATE ENTRANCE\n",
            'You are at the entrance of the park, '
            'You are a electrician and you came to do a checkup\n'
            'You have on you a screwdriver and a flashlight\n'
            'there are paths East, West, Northeast, and Northwest, and South\n',
            'You can\'t go there', 'AIRPLANE', 'LAB', 'VISIT', 'VELO', 'TRI', 'You can\'t go there\n',
            'You can\'t go there')

LAB = Room("LABORATORY\n",
           'You go to the Laboratory and look at how the genetically modify dinosaurs\n'
           'There is a tranquilizer gun on the desk and there is a flare gun on the desk,\n'
           'the tranquilizer has 5 bullets in it while the flare has 3, however you can only take 1\n'
           ' conveniently there is a button with the marking DANGER! on it, and there is a path Northeast\n',
           'You can\'t go there', 'You can\'t go there', 'TRI', 'You can\'t go there', 'You can\'t go there\n',
           'You can\'t go there', 'You can\'t go there', 'You can\'t go there',)

VISIT = Room('VISITOR CENTER\n'
             'You are at the Visitor Center here visitors can buy items,\n'
             'like Odor Away, a net, and bug spray, and a custom Jurrasic Park lighter\n'
             ' there is a path Northwest,\n',
             'You can\'t go there', 'You can\'t go there', 'You can\'t go there', 'You can\'t go there\n',
             'You can\'t go there', 'You can\'t go there', 'VELO', 'You can\'t go there', 'You can\'t go there',)

VELO = Room("VELOCIRAPTOR CAGE\n"
            'You arrive at Velociraptor Valley where you see 4 Velociraptors running around and jumping.\n'
            'They have one huge claw on both of their feet, and they are scared of flares\n.'
            ' There are paths Northeast, North, and West\n',
            'SPINO', 'You can\'t go there', 'TRI', 'You can\'t go there', 'DILOPH', 'You can\'t go there\n',
            'You can\'t go there', 'You can\'t go there', 'You can\'t go there',)

TRI = Room('TRICERATOPS CAGE\n',
           'You arrive at Triceratops Track , there is a Triceratops munching on some leaves,\n'
           'it looks pretty friendly however you should not get close to it,\n'
           '(I feel you can ride it though\n)'
           ' there are paths Northwest, East, and North\n',
           )
