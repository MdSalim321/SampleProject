print("_____Anagram check program____")

def isAnagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

word1 = "Listen"
word2 = "Silent"

if isAnagram(word1, word2):
    print("Anagram")
else:
    print("Not Anagram")

print("______fibbo Series______")

def fibbo(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a+b

fibbo(10)

print("_______factorial____")
def factorial(n):
    fact = 1
    if n ==0 or n ==1:
        return  1
    for i in range(1,n+1):
        fact  = fact *i
    return fact

f = factorial(5)
print(f)

print("_______factorial using recurssion function_____")

def factorials(n):
    fact = 1
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorials(n-1)
print(factorials(5))

print("_________Prime Number Programs________")

def primeNumber(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if primeNumber(100):
    print("Prime Number")
else:
    print("Not Prime number")

