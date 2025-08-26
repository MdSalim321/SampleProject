# Python Program: All Types of Constructors

# 1. Default Constructor
class DefaultConstructor:
    def __init__(self):
        print("Default Constructor: No arguments")


# 2. Parameterized Constructor
class ParameterizedConstructor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Parameterized Constructor: Name={self.name}, Age={self.age}")


# 3. Simulated Overloaded Constructor (using default args)
class OverloadedConstructor:
    def __init__(self, name=None, age=None):
        if name is not None and age is not None:
            print(f"Overloaded Constructor: Name={name}, Age={age}")
        elif name is not None:
            print(f"Overloaded Constructor: Name={name}")
        else:
            print("Overloaded Constructor: No details provided")


# 4. Flexible Constructor using *args
class FlexibleConstructor:
    def __init__(self, *args):
        print(f"Flexible Constructor: Arguments received = {args}")


# ======= Execution =======

print("\n--- 1. Default Constructor ---")
obj1 = DefaultConstructor()

print("\n--- 2. Parameterized Constructor ---")
obj2 = ParameterizedConstructor("Alice", 25)
obj2.display()

print("\n--- 3. Overloaded Constructor ---")
obj3 = OverloadedConstructor()
obj4 = OverloadedConstructor("Bob")
obj5 = OverloadedConstructor("Charlie", 30)

print("\n--- 4. Flexible Constructor ---")
obj6 = FlexibleConstructor()
obj7 = FlexibleConstructor(10)
obj8 = FlexibleConstructor("Python", 3.11, True, [1, 2, 3])
