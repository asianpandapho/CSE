world_map = {
    'AIRPLANE': {
        'NAME': 'AIRPLANE LENDING AREA',
        'DESCRIPTION': 'You are in the airplane landing area, you can only go north to go to the gate.',
        'PATHS': {
            'N': 'GATE'
        }
    },
    'GATE': {
        'NAME': 'GATE ENTRANCE',
        'DESCRIPTION': 'You are at the entrance of the park, '
                       'You are a electrician and you came to do a checkup\n'
                       'You have on you a screwdriver and a flashlight\n'
                       'there are paths East, West, Northeast, and Northwest',
        'PATHS': {
            'NE': 'VELO',
            'E': 'VISIT',
            'W': 'LAB',
            'NW': 'TRI'
        }
    },
    'LAB': {
        'NAME': 'LABORATORY',
        'DESCRIPTION': 'You go to the Laboratory and look at how the genetically modify dinosaurs\n'
                       ' conveniently there is a button with the marking DANGER! on it, there is a path Northeast',
        'PATHS': {
            'NE': 'NORTHEAST',
        }
    },
    'VISIT': {
        'NAME': 'VISITOR CENTER',
        'DESCRIPTION': 'You are at the Visitor Center here visitors can buy items, there is a path Northwest,',
        'PATHS': {
            'NW': 'NORTHWEST',
        }
    },
    'VELO': {
        'NAME': 'VELOCIRAPTOR CAGE',
        'DESCRIPTION': 'You arrive at the Velociraptor Cage where you see 4 Velociraptors running around and jumping.\n'
                       ' There are paths Northeast, North, and West',
        'PATHS': {
            'NW': 'NORTHEAST',
            'N': 'NORTH',
            'W': 'WEST'
        }
    },
    'TRI': {
        'NAME': 'TRICERATOPS CAGE',
        'DESCRIPTION': 'You arrive at the Triceratops Cage, there is a Triceratops munching on some leaves,\n'
                       ' there are paths Northwest, East, and North',
        'PATHS': {
            'NW': 'NORTHWEST',
            'N': 'NORTH',
            'E': 'EAST'
        }
    },
    'BRACHIO': {
        'NAME': 'BRACHIOSAURUS CAGE',
        'DESCRIPTION': 'You arrive at the Brachiosaurus Cage, you see huge dinosaurs walking around and eating from\n'
                       ' massive trees, there are paths West, East, and North',
        'PATHS': {
            'W': 'WEST',
            'N': 'NORTH',
            'E': 'EAST'
        }
    },
    'SPINO': {
        'NAME': 'SPINOSAURUS CAGE',
        'DESCRIPTION': 'You arrive at the Spinosaurus Cage and see a huge Spinosaurus, it look very hungry,\n'
                       ' there are paths East, North, and West',
        'PATHS': {
            'W': 'WEST',
            'N': 'NORTH',
            'E': 'EAST'
        }
    },
    'DILOPH': {
        'NAME': 'DILOPHOSAURUS CAGE',
        'DESCRIPTION': 'You arrive at the Dilophosaurus Cage and see 4 Dilophosaurus fighting,\n'
                       'and they look very hungry, there are paths West and Northwest',
        'PATHS': {
            'W': 'WEST',
            'NW': 'NORTHWEST'
        }
    },
    'MEGA': {
        'NAME': 'MEGALODON CAGE',
        'DESCRIPTION': 'You arrive at the Dilophosaurus Cage and see 4 Dilophosaurus fighting,\n'
                       'and they look very hungry, there are paths West and Northwest',
        'PATHS': {
            'W': 'WEST',
            'NW': 'NORTHWEST'
        }
    },
    'T REX': {
        'NAME': 'TYRANNOSAURUS CAGE',
        'DESCRIPTION': 'You arrive at the Tyrannosaurus Rex Cage, there you see the king of dinosaurs,\n'
                       ' there are paths North and West',
        'PATHS': {
            'W': 'WEST',
            'N': 'NORTH'
        }
    },
    'STEGO': {
        'NAME': 'STEGOSAURUS CAGE',
        'DESCRIPTION': 'You arrive at the Stegosaurus Cage, you see the stegosaurus drinking water,\n'
                       ' there are paths North and East',
        'PATHS': {
            'E': 'EAST',
            'N': 'NORTH'
        }
    },
    'I REX': {
        'NAME': 'INDOMINOUS REX CAGE',
        'DESCRIPTION': 'You arrive at the Indominous Rex Cage, you cant see anything but trees,\n'
                       ' however you feel a presence, there are paths Northwest and West',
        'PATHS': {
            'W': 'WEST',
            'NW': 'NORTHWEST'
        }
    },
    'COPTER': {
        'NAME': 'HELIPAD',
        'DESCRIPTION': 'You arrive at the Helipad, you get onto the helicopter and leave the Island.',
    }
}

while
    current_node = world_map["AIRPLANE"]
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])


# Anou Her
