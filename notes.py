# import random
#
# print("Hello World")
#
# # print ("Anou Is Asian Daddy")
#
# print(3 + 5)
# print(5 - 3)
# print(5 * 3)
# print(6 / 2)
# print(3 ** 2)
# print()  # Create a blank line
# print("See if you can figure this out")
# print(13 % 12)
# print(15 % 5)
# print(5 % 3)
# print(14 % 14)
# print(-12 % 2)
# print(1 % 1)
# print(1004 % 13)
#
# # # Variable
# # car_name = "Anou Mobile for you to DRIVE"
# # car_type = "Lamborghini Aventador Sesto Elemento Honda Subaru"
# # car_cylinders = 8
# # car_mpg =  9000.1
# #
# # # Inline Printing
# # print ("My car is a Honda Civic %s " % car_name)
# # print ("My car is the %s. It is a %s" % (car_name, car_type))
# #
# # # Taking Input
# # name = input ("What is your name?")
# # print ("Hello %s" % name)
# # print(name)
# # # print (name)
# # age = input ("What is your age?")
# # print ("You are %s" % age)
# # print(age)
# #
# #
# # # Change to the file
# #
# # def print_hw():
# #     print ("Hello World")
# #
# #
# # print_hw()
# #
# #
# # def say_hi(name): #name is a "paramater"
# #     print("Hello %s." % name)
# #     print("I hope you have a fantastic day")
# #
# #
# # say_hi
# #
# #
# # def birthday (age):
# #     age += 1 # age = age + 1
# #
# # say_hi ("John")
# # print ("John is 15. Next Year.")
# # birthday(15)
#
# # Press Ctrl-A and Ctrl-/
# # to comment old code
#
#
# def f(x):
#     return x**5 + 4 + x ** 4 - 17*x**2 + 4
#
#
# print(f(3) + f(5))
#
# # If statements
#
#
# def grade_calc(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80:
#         return "B"
#     elif percentage >= 70:
#         return "C"
#     elif percentage >= 60:
#         return 'D'
#     else:
#         return "F"
# #
# # #     Loops
# #
# #
# # for num in range(5):
# #     print (num + 1)
#
#
# # for yo in "in":
# #     print (yo)
#
# a = 1
# while a <= 10:
#     print(a)
#     a += 1
#
# # response = ""
# # while response != "Hello":
# #     response = input("Say \"Hello\"")
#
#
# print("Hello \nWorld")  # \n means new line
#
#
# print(random.randint(0, 6))
#
# # Comparisons
# print(1 == 1)  # Two equal signs to compare
# print(1 != 2)  # One is not equal to two
# print(not False)  # This prints true
# print(1 == 1 and 4 <= 5)
# print(1 < 0 or 5 > 1)
#
# # Recasting
# c = "1"
# print(c == 1)  # False - c is a string, 1 is a int
# print(int(c) == 1)  # True - Compares two ints
# print(c == str(1))  # True - Compares two strings

# the_count = [1, 2, 3, 4, 5]
# shopping_list = ["Noodles", "Eggrolls", "Milk", "Rice", "Soda", "Chips"]
#
# print(len(shopping_list))
#
# # Going through a list
# for item in shopping_list:
#     print(item)
#
# for num in the_count:
#     print(num ** 2)
#
# len(shopping_list)  # Gives me the length of the list XD
# range(3)  # Gives a list of the numbers 0 through 2
# range(len(shopping_list))  # A list of EVERY index in a list
#
# for num in range(len(shopping_list)):
#     item = shopping_list[num]
#     print("The item at index %d is %s" % (num, item))
#
# # Turn things into a list
# str1 = "Hello Class!"
# listOne = list(str1)
# print(listOne)
# listOne[11] = "."
# print(listOne)
# newStr = ("■".join(listOne))
# print(newStr)
#
#
# # Add things to a list
# shopping_list.append("Cereal")
# print(shopping_list)
#
# # Remove things from a list
# shopping_list.remove("Soda")
# print(shopping_list)
# shopping_list.pop(0)
# print(shopping_list)
#
# # The string Class
#
# import string
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.punctuation)
# print(string.digits)
#
# # Dealing with strings
# strTwo = "tHIs iS a vEry ODd seNTeNce"
# lowercase = strTwo.lower()
# print(lowercase)

# Dictionaries - Make up a key value pair
dictionary = {"name": "lance", "age": "18", "height": 6 * 12 + 2}

# Processing from a dictionary
print(dictionary['name'])
print(dictionary['age'])
print(dictionary["height"])

large_dictionary = {
    'California': 'CA',
    "Minnesota": 'MI',
    'Florida': "FL",
    'Illinois': 'IL'
}
larger_dictionary = {
    'California': [
        "Fresno",
        "Sacramento",
        "Orange County"
    ],

    "Washington": [
        "Seattle",
        "Tacoma",
        "Olympia",
        "Spokane"
    ],
    'Illinois': [
        "Chicago",
        "Naperville",
        "Peora"
    ],
    "Florida": [
        "Miami",
        "Town"
        "Another town in Florida"
        ]
}
print(large_dictionary['Florida'])
print(larger_dictionary["Illinois"][0])
print(larger_dictionary['Washington'][3])
# Spokane
largest_dictionary = {
    "CA": {
        'NAME': "California",
        "POPULATION": 3925000,
        'BORDER ST':  [
            'OREGON',
            'NEVADA',
            'ARIZONA'
        ],
    },
    "MI": {
        'NAME': "Michigan",
        "POPULATION": 9928000,
        'BORDER ST': [
            'Wisconsin',
            'Ohio',
            'Indiana'
        ],
    'FL':{
        "NAME": "Florida"
    }
    }
}
print(largest_dictionary["MI"]["BORDER ST"][2])
