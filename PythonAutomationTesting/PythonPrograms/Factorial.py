def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
fact = factorial(num)
print( f"factorial of {num} is {fact}" )
