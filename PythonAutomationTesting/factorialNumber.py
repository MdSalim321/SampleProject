def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage

n = int(input("enter a number: ")) # Change this number as needed
fact = factorial(n)
print("Factorial of", n, "is:",fact)
