class Animal:
    def sound(self):
        print("Animal sounds in parent class")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog bark in the child class")

class Cat(Animal):
    def sound(self):
        super().sound()
        print("Cat mauee in the child class")

class Rat(Animal):
    def sound(self):
        super().sound()
        print("Rat sounds kismish in the chuld class ")


d = Dog()
d.sound()
c = Cat()
c.sound()
r = Rat()
r.sound()