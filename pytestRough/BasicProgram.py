class Addition:
    def __init__(self, a, b):
        self.a =a
        self.b =b
        print(self.a-self.b)

print("enter two number: ")
x= float(input("enter 1st number: "))
y = float(input("enter 2nd number: "))
obj = Addition(x,y)
