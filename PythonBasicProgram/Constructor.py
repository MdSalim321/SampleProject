class DefaultConstructor:
    def __init__(self):
        print("Default constructor")

d = DefaultConstructor()

class ParameterisedConstructor:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks



    def display(self):
        print(f"name is: {self.name} \nroll number is: {self.roll}\nmarks is: {self.marks}")

obj = ParameterisedConstructor("Bhai", 1, 100)
obj.display()



class ConstructorOverloading():
    def __init__(self, name = None, roll = None):
        if name is not None and roll is not None:
            print(f"name is: {name}\n roll is: {roll}")
        elif name is not None:
            print(f"name is: {name}")
        else:
            print("No details provided")


class ConstructorFlexible:
    def __init__(self, *args):
        print("Arguments received ", args)


obj1 = ConstructorFlexible()
obj2 = ConstructorFlexible(10, "Bhai", True)
obj3 = ConstructorFlexible("Selim", 10)


obj1 = ConstructorOverloading()
obj2 = ConstructorOverloading("Brother")
obj3 = ConstructorOverloading("Brother", 10)




