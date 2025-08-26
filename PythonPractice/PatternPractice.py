print("____Pyramid Print____")
def pyramid(n):
    for i in range(n):
        for j in range(i, n):
            print(" ", end="")
        for j in range(i+1):
            print("*", end="")
        for j in range(i):
            print("*", end="")
        print("")

pyramid(5)

print("_________Variable length Arguments___________")

def average(*t):
    avg = sum(t)/len(t)
    return avg
result1 = average(12,23,34,45,67,78,89)
result2 = average(98,87,76,65,54,43,32,21)
print(result1)
print(result2)

print("_________kwargs of variable length________")
def average_with_kwargs(** kwargs):
    values = list(kwargs.values())
    avgs = sum(values)/len(values)
    return avgs

result1 = average_with_kwargs(nam1= 12, num2= 23, num3 = 34, num4= 45, num5=56)
result2 = average_with_kwargs(val1= 87, val2= 76, val3= 65, val4= 54, val=43, vall=32)

print(result1)
print(result2)

print("________Creating Instance member variable_______")

class Test:
    def __init__(self):
        self.a = 5

    def func(self):
        self.b = 10

t1 = Test()
t2 = Test()
t1.func()
t2.func()
print(t1.__dict__)
print(t2.__dict__)

print("_______Lamda Function_______")
f = lambda a, b : a+b
r = f(3,7)
print(r)

print("_____lamda Function in single line_______")
print(f"Addition of a & b is: ", (lambda a,b: a+b)(5,6))

print("______Substraction_______")
sub = lambda a, b: a-b
s= sub(6,8)
print("Subtraction is: ",s)

print("______multiplication______")
mul = lambda a, b: a*b
m = mul(12, 3)
print("Multiplication is: ",m)

print("_______Division________")
div = lambda a, b: a/b
d = div(12, 3)
print("Division is: ", d)

print("______Factorial using the Division_______")
fact = lambda n: 1 if n == 0 else n*fact(n-1)
f= fact(4)
print("Factorial is: ", f)

print("______List of Even numbers________")
l1 = [5*e for e in range (1,100)]
print(l1)

print("____Even number print from the list_____")
lst = [23,34,45,56,67,78,89]
l2 = [e for e in lst if e%2 ==0]
print(l2)

print("____Check a string is palindrome or not_____")

isPalindrome = lambda s : s == s[::-1]

print(isPalindrome("madam"))
print(isPalindrome("hello"))

print("________Check a number is palindrome or not______")

isPalindromeNumber = lambda n : str(n) == str(n)[::-1]

print(isPalindromeNumber(123))
print(isPalindromeNumber(1221))

print("______Factorial using Lambda function____")

factorial = lambda n: 1 if n == 0 else n * factorial(n-1)
print(factorial(4))


print("______To check a number is prime or not_________")
n =int(input("Enter a number: "))
if  n > 1:
    for i in range(2, n):
        if n% i == 0:
            print(f"{n} is not a prime Number: ")
            break

    else:
        print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")







