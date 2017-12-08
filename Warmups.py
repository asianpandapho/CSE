# 12.4.17


def reverse_order(first_name, last_name):
    # print("%s %s" % (last_name, first_name))
    print(last_name + " " + first_name)  # Concatenation

#
# def reverse_order():
#     first_name = input("What is your first name?")
#     last_name = input("What is your last name?")
#


"""Warmup #2

Write a function called "happy_bday"
that 'sings' (prints)
the Happy Birthday Song

It must take one parameter called "name"

"""


def happy_bday(name):
    print("Happy Birthday to You,")
    print("Happy Birthday to You,")
    print("Happy Birthday dear %s" + name)
    print("Happy Birthday to You!")


# 12.5.17
"""Write a function called add_py
that takes one parameter called "name"
and prints out name.py
example:
add_py("I_ate_some") = "I_ate_some.py"
"""


def add_py(name):
    print("%s.py" % name)  # Solution Juan
    print(name + ".py")  # Solution Dos


# 12.6.17
"""Write a function called "add"
which takes three parameters
and print the sum of the numbers
"""


# def add(juan, dos, tres):
#     print(int(juan + dos + tres))
#
#
# add(90, 900, 9000)


def repeat(string):
    print(string)
    print(string)
    print(string)

    for x in range(3):
        print(string)


def date(month, day, year):
    print(str(month) + "/" + str(day) + str(year))


print(12, 8, 17)
