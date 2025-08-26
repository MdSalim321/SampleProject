class MethodOverload:
    def add(self,*args):
        return sum(args)

numbers = []
print("Enter 5 numbers: ")
for i in range(5):
    values = int(input(f"Enter values {i}: "))
    numbers.append(values)

obj = MethodOverload()
sum = obj.add(*numbers)
print(sum)


