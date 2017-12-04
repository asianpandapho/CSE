# 12.4.17


def reverse_order (first_name, last_name):
    # print("%s %s" % (last_name, first_name))
    print(last_name + " " + first_name)  # Concatenation


def reverse_order():
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")


"""Warmup #2

Write a function called "happy_bday"
that 'sings' (prints)
the Happy Birthday Song

It must take one parameter called "name"

"""



def happy_bday(name):
    print ("Happy Birthday to You,")
    print("Happy Birthday to You,")
    print ("Happy Birthday dear %s" + name)
    print ("Happy Birthday to You!")

