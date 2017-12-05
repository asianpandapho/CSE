import random

print("Hello World")

# print ("Anou Is Asian Daddy")

print(3 + 5)
print(5 - 3)
print(5 * 3)
print(6 / 2)
print(3 ** 2)
print()  # Create a blank line
print("See if you can figure this out")
print(13 % 12)
print(15 % 5)
print(5 % 3)
print(14 % 14)
print(-12 % 2)
print(1 % 1)
print(1004 % 13)

# # Variable
# car_name = "Anou Mobile for you to DRIVE"
# car_type = "Lamborghini Aventador Sesto Elemento Honda Subaru"
# car_cylinders = 8
# car_mpg =  9000.1
#
# # Inline Printing
# print ("My car is a Honda Civic %s " % car_name)
# print ("My car is the %s. It is a %s" % (car_name, car_type))
#
# # Taking Input
# name = input ("What is your name?")
# print ("Hello %s" % name)
# print(name)
# # print (name)
# age = input ("What is your age?")
# print ("You are %s" % age)
# print(age)
#
#
# # Change to the file
#
# def print_hw():
#     print ("Hello World")
#
#
# print_hw()
#
#
# def say_hi(name): #name is a "paramater"
#     print("Hello %s." % name)
#     print("I hope you have a fantastic day")
#
#
# say_hi
#
#
# def birthday (age):
#     age += 1 # age = age + 1
#
# say_hi ("John")
# print ("John is 15. Next Year.")
# birthday(15)

# Press Ctrl-A and Ctrl-/
# to comment old code


def f(x):
    return x**5 + 4 + x ** 4 - 17*x**2 + 4


print(f(3) + f(5))

# If statements


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return 'D'
    else:
        return "F"

#     Loops


# for num in range(5):
#     print (num + 1)


# for yo in "in":
#     print (yo)

a = 1
while a <= 10:
    print(a)
    a += 1

# response = ""
# while response != "Hello":
#     response = input("Say \"Hello\"")


print("Hello \nWorld")  # \n means new line


print(random.randint(0, 6))

# Comparisons
print(1 == 1)  # Two equal signs to compare
print(1 != 2)  # One is not equal to two
print(not False)  # This prints true
print(1 == 1 and 4 <= 5)
print(1 < 0 or 5 > 1)

# Recasting
c = "1"
print(c == 1)  # False - c is a string, 1 is a int
print(int(c) == 1)  # True - Compares two ints
print(c == str(1))  # True - Compares two strings

