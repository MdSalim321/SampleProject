import decimal


integer = 10
print(decimal.Decimal(integer))
print(type(decimal.Decimal(integer)))

string = '12345'
print(decimal.Decimal(string))
print(type(decimal.Decimal(string)))

string = "Python Programming"
print(string[::-1])

vowels = ['a', 'e','i', 'o','u']
word = "Programming Language"
count = 0

for charecter in word:
    if charecter in vowels:
        count+=1

print(count)

vowels = ['a', 'e', 'i', 'o', 'u']
word = "PROGRAMMINGLANGUAGE"
print(word.lower())

l = len(word)
print(l)
count = 0

for char in word:
    if char not in vowels:
        count +=1

print(count)

