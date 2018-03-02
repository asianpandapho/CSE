# Defining a class
# class Shoes(object):
#     def __init__(self, lace_color, lighting, brand):  # TWO underscores before and after
#         # Things a shoe has
#         self.lace_color = lace_color
#         self.rgb_lighting = lighting
#         self.used = False
#         self.brand = brand
#         self.clean = True
#
#     def wear(self):
#         self.used = True
#         self.clean = False
#         print('You wear the shoes')
#
#     def wash(self):
#         self.clean = True
#         print("You cleaned the shoes")
#
#
# first_pair = Shoes("Red", "True", "Sketchers")
# second_pair = Shoes("Blue", "True", "Reebok")
#
# print(first_pair.brand)
# print(second_pair.lace_color)
# print(first_pair.clean)
#
# first_pair.wear()
# print(first_pair.clean)
# first_pair.wash()
# print(first_pair.clean)


class Car(object):
    def __init__(self, color, rims, brand, model, horsepower, running):
        self.color = color
        self.washed = True
        self.rims = rims
        self.brand = brand
        self.used = False
        self.model = model
        self.horsepower = horsepower
        self.running = running
    # Hai

    def drive(self):
        self.used = True
        self.washed = False
        print("You go for a ride")

    def clean(self):
        self.washed = True
        print('You washed your car')

    def drive_forward(self):
        if self.running:
            print('You have moved forward')
        else:
            print("Nothing Happens")

    def turn_on(self):
        if self.running:
            print("Nothing happens")
        else:
            self.running = True
            print("You started the car")

    def turn_off(self):
        if self.running:
            print("Nothing happens")
        else:
            self.running = False
            print("Your car is not on")


mycoolcar = Car(4, "Blue", "Gold" "Lambo", "100", "True", "True")
mycoolcar.turn_on()
mycoolcar.drive_forward()
mycoolcar.turn_off()

