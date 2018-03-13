class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work." % self.name)


class Employee(Person):
    def __init__(self, name, age, job):
        super(Employee, self).__init__(name, age)
        self.job = job

    def job(self):
        print("He makes %s" % self.job)


class Programmer(Employee):
    def __init__(self, name, age, job, computer):
        super(Programmer, self).__init__(name, age, job)
        self.computer = computer

    def comp(self):
        print('He uses an %s' % self.computer)


steve = Employee("Steve", 29, 'Food')
Employee.work(steve)
Employee.job(steve)

Weibe_Chan = Programmer("Weibe-Sama", 900, 'Games', 'Alienware Aurora')
Programmer.work(Weibe_Chan)
Programmer.job(Weibe_Chan)
Programmer.comp(Weibe_Chan)
