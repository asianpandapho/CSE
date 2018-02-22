# # Defining a class
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


class Car(object):
    def __init__(self, color, brand, model, horsepower):
        self.color = color
        self.washed = True
        self.brand = brand
        self.model = model
        self.horsepower = horsepower
        self.used = False
        self.running = False
        self.notrunning = True
        self.passengers = 0
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
        if self.notrunning:
            print("You turned off the car car")
            self.used = True

    def go_for_a_drive(self, passengers):
        print("%d passingers get in" % passengers)
        self.passengers = passengers
        self.turn_on()
        self.drive()
        self.drive()
        self.drive()
        self.turn_off()
        print("%d passenger got off" % passengers)
        self.passengers = 0


my_car = Car("Green", "Lamboghini", "X", 9000)
my_car.go_for_a_drive(4)
