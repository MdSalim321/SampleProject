class Person:
    def display(self):
        print("I am a person")

class Employee(Person):
    def display(self):
        super().display()
        print("I am in child Employee class")

class FreeLancer:
    def display(self):
        print("I am a freelancer")

class Developer(Employee, FreeLancer):
    def display(self):
        super().display()
        FreeLancer.display(self)
        print("I am in child Developer class")

d = Developer()
d.display()

