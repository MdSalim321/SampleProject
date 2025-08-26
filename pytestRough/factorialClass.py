class Factorial:
    def facts(self, n):
        if n == 0:
            return 1
        else:
            return n* self.facts(n-1)

obj = Factorial()
num = int(input("Enter a number: "))
result = obj.facts(num)
print(f"Factorial of {num} is: ", result)