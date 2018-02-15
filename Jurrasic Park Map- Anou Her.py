world_map = {
    'AIRPLANE': {
        'NAME': 'AIRPLANE LANDING AREA',
        'DESCRIPTION': 'You are in the airplane landing area, you can only go North to go to the gate.',
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
                       'There is a tranquilizer gun on the desk and there is a flare gun on the desk,\n'
                       'the tranquilizer has 5 bullets in it while the flare has 3, however you can only take 1\n'
                       ' conveniently there is a button with the marking DANGER! on it, and there is a path Northeast',
        'PATHS': {
            'NE': 'TRI',
        }
    },
    'VISIT': {
        'NAME': 'VISITOR CENTER',
        'DESCRIPTION': 'You are at the Visitor Center here visitors can buy items,\n'
                       'like Odor Away, a net, and bug spray, and a custom Jurrasic Park lighter\n'
                       ' there is a path Northwest,',
        'PATHS': {
            'NW': 'VELO',
        }
    },
    'VELO': {
        'NAME': 'VELOCIRAPTOR CAGE',
        'DESCRIPTION': 'You arrive at Velociraptor Valley where you see 4 Velociraptors running around and jumping.\n'
                       'They have one huge claw on both of their feet, and they are scared of flares.'
                       ' There are paths Northeast, North, and West',
        'PATHS': {
            'NE': 'DILOPH',
            'N': 'SPINO',
            'W': 'TRI'
        }
    },
    'TRI': {
        'NAME': 'TRICERATOPS CAGE',
        'DESCRIPTION': 'You arrive at Triceratops Track , there is a Triceratops munching on some leaves,\n'
                       'it looks pretty friendly however you should not get close to it,\n'
                       '(I feel you can ride it though)'
                       ' there are paths Northwest, East, and North',
        'PATHS': {
            'NW': 'MEGA',
            'N': 'BRACHIO',
            'E': 'VELO'
        }
    },
    'BRACHIO': {
        'NAME': 'BRACHIOSAURUS CAGE',
        'DESCRIPTION': 'You arrive at Brachiosaurus Bridge, you see huge dinosaurs walking around and eating from\n'
                       ' massive trees, there are paths West, East, and North',
        'PATHS': {
            'W': 'MEGA',
            'N': 'STEGO',
            'E': 'SPINO'
        }
    },
    'SPINO': {
        'NAME': 'SPINOSAURUS CAGE',
        'DESCRIPTION': 'You arrive at Spinosaurus Station and see a huge Spinosaurus, it look very hungry,\n'
                       'you don\'t want to mess with it, however 2 trang bullets will make it unconscious'
                       ' there are paths East, North, and West',
        'PATHS': {
            'W': 'BRACHIO',
            'N': 'T REX',
            'E': 'DILOPH'
        }
    },
    'DILOPH': {
        'NAME': 'DILOPHOSAURUS CAGE',
        'DESCRIPTION': 'You arrive at Dilophosaurus Dungeon and see 4 Dilophosaurus fighting,\n'
                       'and they look very hungry, they can all be scared off by a flare if you shoot it properly\n'
                       'there are paths West and Northwest',
        'PATHS': {
            'W': 'SPINO',
            'NW': 'T REX'
        }
    },
    'MEGA': {
        'NAME': 'MEGALODON CAGE',
        'DESCRIPTION': 'You arrive at Megalodon Waters and see 1 huge shark in the water,\n'
                       'it looks like it can jump out at you at any second,\n'
                       'but it remains calm for now just don\t drop blood into the water'
                       'there are paths East and Northeast',
        'PATHS': {
            'E': 'BRACHIO',
            'NE': 'STEGO'
        }
    },
    'T REX': {
        'NAME': 'TYRANNOSAURUS CAGE',
        'DESCRIPTION': 'You arrive at the Tyrannosaurus Jungle, there you see the king of dinosaurs,\n'
                       'it can be tranquilized with 3 tranq bullets,\n'
                       ' there are paths North and West',
        'PATHS': {
            'W': 'STEGO',
            'N': 'I REX'
        }
    },
    'STEGO': {
        'NAME': 'STEGOSAURUS CAGE',
        'DESCRIPTION': 'You arrive at Stegosaurus Acres, you see the stegosaurus drinking water,\n'
                       'you might need to befriend it later\n'
                       ' there are paths North and East',
        'PATHS': {
            'E': 'T REX',
            'N': 'PTER'
        }
    },
    'I REX': {
        'NAME': 'INDOMINOUS REX CAGE',
        'DESCRIPTION': 'You arrive at Indominous Rex Swamp, you cant see anything but trees,\n'
                       ' however you feel a presence someone told you that the I Rex can be tranquilized by 5 darts\n'
                       ', there are paths Northwest and West',
        'PATHS': {
            'W': 'PTER',
            'NW': 'COPTER'
        }
    },
    'PTER': {
        'NAME': 'PTERODACTYL CAGE',
        'DESCRIPTION': 'You arrive at Pterodactyl City, you see them fly in the sky,\n'
                       'it looks like they can just swoop down an grab you off the ground, a flare can scare them off\n'
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
long_directions = ['NORTH', 'EAST', 'SOUTH', 'WEST', 'NORTHEAST', 'NORTHWEST', 'SOUTHEAST', 'SOUTHWEST']

while True:
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])
    command = input('>_').upper()
    if command == 'QUIT':
        quit(0)
    if command in long_directions:
        index = long_directions.index(command)
        command = directions[index]
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print('You cannot go this way')
    else:
        print('command not Recognized')
    if current_node == world_map["COPTER"]:
        print('You arrive at the Helipad, you get onto the helicopter and leave the Island. GOOD JOB!')
        exit(0)

# Anou Her
