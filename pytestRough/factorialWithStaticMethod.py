class Factorial:
    @staticmethod
    def facts(n):
        if n == 0:
            return 1
        else:
            return n * Factorial.facts(n - 1)

num = int(input("Enter a number: "))
result = Factorial.facts(num)
print(f"Factorial of {num} is: {result}")
