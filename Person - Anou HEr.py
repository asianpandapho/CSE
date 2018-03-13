class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, age):
        super(Employee, self).__init__(name, age)
        self.job = job


class Programmer(Person):
    def __init__(self, name, age):
        super(Programmer, self).__init__(name, age)


steve = Employee("Steve", 29)
Employee.work(steve)

Weibe_Chan = Programmer("Weibe-Sama", 900)
Programmer.work(Weibe_Chan)