world_map = {
    'AIRPLANE': {
        'NAME': 'AIRPLANE LENDING AREA',
        'DESCRIPTION': 'You are in the airplane landing area, you can only go north to go to the gate.\n'
                       'Use N,S,W,E, NE, NW, SE, SW to move.',
        'PATHS': {
            'N': 'GATE'
        }
    },
    'GATE': {
        'NAME': 'GATE ENTRANCE',
        'DESCRIPTION': 'You are at the entrance of the park, '
                       'You are a electrician and you came to do a checkup\n'
                       'You have on you a screwdriver and a flashlight\n'
                       'there are paths East, West, Northeast, and Northwest, and South',
        'PATHS': {
            'NE': 'VELO',
            'E': 'VISIT',
            'W': 'LAB',
            'NW': 'TRI',
            'S': 'AIRPLANE'
        }
    },
    'LAB': {
        'NAME': 'LABORATORY',
        'DESCRIPTION': 'You go to the Laboratory and look at how the genetically modify dinosaurs\n'
                       ' conveniently there is a button with the marking DANGER! on it, there is a path Northeast',
        'PATHS': {
            'NE': 'TRI',
        }
    },
    'VISIT': {
        'NAME': 'VISITOR CENTER',
        'DESCRIPTION': 'You are at the Visitor Center here visitors can buy items, there is a path Northwest,',
        'PATHS': {
            'NW': 'VELO',
        }
    },
    'VELO': {
        'NAME': 'VELOCIRAPTOR CAGE',
        'DESCRIPTION': 'You arrive at the Velociraptor Cage where you see 4 Velociraptors running around and jumping.\n'
                       ' There are paths Northeast, North, and West',
        'PATHS': {
            'NE': 'DILOPH',
            'N': 'SPINO',
            'W': 'TRI'
        }
    },
    'TRI': {
        'NAME': 'TRICERATOPS CAGE',
        'DESCRIPTION': 'You arrive at the Triceratops Cage, there is a Triceratops munching on some leaves,\n'
                       ' there are paths Northwest, East, and North',
        'PATHS': {
            'NW': 'MEGA',
            'N': 'BRACHIO',
            'E': 'VELO'
        }
    },
    'BRACHIO': {
        'NAME': 'BRACHIOSAURUS CAGE',
        'DESCRIPTION': 'You arrive at the Brachiosaurus Cage, you see huge dinosaurs walking around and eating from\n'
                       ' massive trees, there are paths West, East, and North',
        'PATHS': {
            'W': 'MEGA',
            'N': 'STEGO',
            'E': 'SPINO'
        }
    },
    'SPINO': {
        'NAME': 'SPINOSAURUS CAGE',
        'DESCRIPTION': 'You arrive at the Spinosaurus Cage and see a huge Spinosaurus, it look very hungry,\n'
                       ' there are paths East, North, and West',
        'PATHS': {
            'W': 'BRACHIO',
            'N': 'T REX',
            'E': 'DILOPH'
        }
    },
    'DILOPH': {
        'NAME': 'DILOPHOSAURUS CAGE',
        'DESCRIPTION': 'You arrive at the Dilophosaurus Cage and see 4 Dilophosaurus fighting,\n'
                       'and they look very hungry, there are paths West and Northwest',
        'PATHS': {
            'W': 'SPINO',
            'NW': 'T REX'
        }
    },
    'MEGA': {
        'NAME': 'MEGALODON CAGE',
        'DESCRIPTION': 'You arrive at the Dilophosaurus Cage and see 4 Dilophosaurus fighting,\n'
                       'and they look very hungry, there are paths East and Northeast',
        'PATHS': {
            'E': 'BRACHIO',
            'NE': 'STEGO'
        }
    },
    'T REX': {
        'NAME': 'TYRANNOSAURUS CAGE',
        'DESCRIPTION': 'You arrive at the Tyrannosaurus Rex Cage, there you see the king of dinosaurs,\n'
                       ' there are paths North and West',
        'PATHS': {
            'W': 'STEGO',
            'N': 'I REX'
        }
    },
    'STEGO': {
        'NAME': 'STEGOSAURUS CAGE',
        'DESCRIPTION': 'You arrive at the Stegosaurus Cage, you see the stegosaurus drinking water,\n'
                       ' there are paths North and East',
        'PATHS': {
            'E': 'T REX',
            'N': ''
        }
    },
    'I REX': {
        'NAME': 'INDOMINOUS REX CAGE',
        'DESCRIPTION': 'You arrive at the Indominous Rex Cage, you cant see anything but trees,\n'
                       ' however you feel a presence, there are paths Northwest and West',
        'PATHS': {
            'W': 'PTER',
            'NW': 'COPTER'
        }
    },
    'PTER': {
        'NAME': 'PTERODACTYL CAGE',
        'DESCRIPTION': 'You arrive at the Pterodactyl Cage, you see them fly in the sky,\n'
                       ' there are paths Northeast and East',
        'PATHS': {
            'E': 'I REX',
            'NE': 'COPTER'
        }
    },
    'COPTER': {
        'NAME': 'HELIPAD',
        'DESCRIPTION': 'You arrive at the Helipad, you get onto the helicopter and leave the Island.',
    }
}

current_node = world_map["AIRPLANE"]
directions = ['N', 'E', 'S', 'W', 'NE', 'NW', 'SE', 'SW']

while True:
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print('You cannot go this way')
    else:
        print('command not Recognized')

# Anou Her
