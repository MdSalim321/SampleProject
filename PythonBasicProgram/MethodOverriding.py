class Animal:
    def sound(self):
        print("Animal sounds")



class Dog(Animal):
    def sound(self):
        super().sound()

d = Dog()
d.sound()