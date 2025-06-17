x = 20.5
print(x)
print(type(x))

y = int(x)
print(y)
print(type(y))

z = "3j"
print(z)
print(type(z))

t = 3.8
print(t)
print(type(t))

print(type(int(t)))

p = 3.5
print(type(p))
str(p)
print(type(str(p)))

a = "Hello world"
print(a)
print(len(a))

b = "The best things in life is free"
print('LIFE' in b)

c = "The best things in life are free!"
if "free" in c:
  print("Yes, 'free' is present.")


d = "This is a text, & the text is the main aim of life is to be happy"
if 'happy' in d:
  print("Yes, Happy present in the list")

d = "This is a text, & the text is the main aim of life is to be happy"
if 'Courage' not in d:
  print("'Yes', Courage is not present in the text")

e = "This is the text"
print(e[:10])

f = ' This  is  the   text '
print(f.upper())
print(f.lower())
# It removes the extra whiteSpace from begining & ending
print(f.strip())

print(f.replace('t', 'S'))



