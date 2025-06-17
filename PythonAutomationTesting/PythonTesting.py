class Test:
    x = 5
ob1 = Test()
print(ob1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}{self.age}"

P1 = Person("Jhon", 36)

print(P1)

