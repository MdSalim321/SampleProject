print("_____To Check a number is palindrome or not______")

def PalindromeNumber(n):
    m = n
    sum = 0
    while n > 0:
        r = n% 10
        sum = 10* sum + r
        n //=10
    print(sum)
    if(sum == m):
        print("Palindrome Number")
    else:
        print("Not Palindrome numbers")


PalindromeNumber(122)

print("_____Addition using Lambda function______")

add = lambda a, b: (a+b)
a = add(12, 12)
print(a)

print("_____factorial using lambda function______")
fact= lambda n : 1 if n == 0 else n *fact(n-1)

print(fact(5))

print("________Spy Number______")
'''sum of digit, if equql to product of digit'''

def spyNumber(n):
    sum = 0
    prod = 1
    while n> 0:
        r = n % 10
        sum = sum + r
        prod = r * prod
        n //= 10
    if(prod == sum):
        print("Spy Number")

    else:
        print(" Not Spy Number ")

spyNumber(122)

print("________DuckNumber_______")
def duckNumber(n):
    m = n
    count =0
    while n != 0:
        r = n%10
        n //=10
        if r ==0:
            count +=1

    if(count>1):
        print("Duck NUmber")
    else:
        print("Not Duck number")

duckNumber(123)

print("_______Amstrong Number_________")

def amstrongNumber(n):
    m= n
    sum = 0
    while n > 0:
        r = n % 10
        sum = sum + r **3
        n //=10

    if(m == sum):
        print("Amstrong Number")
    else:
        print("Not Amstrong Number")

amstrongNumber(153)

print(" _____Krishna Murthy Special Number____")
import math
def krishnaMurthyNumber(n):
    m = n
    sum = 0
    while n > 0:
        r = n % 10
        sum = sum + math.factorial(r)
        n //= 10
    if(m == sum):
        print("Krishna Murthy Special Number")
    else:
        print(" Not Krishna Murthy Special Number")

krishnaMurthyNumber(146)

