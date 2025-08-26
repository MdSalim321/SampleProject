def factotial(n):
    if n ==1:
        return 1
    else:
        return n * factotial(n-1)

num = int(input("Enter a number"))
fact = factotial(num)
print(fact)