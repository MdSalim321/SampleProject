tup = (1,2,3,4,4)
print(tup)
print(tup[0])
print(tup[3])
print(tup[-1])
print(tup[2:4])
print(5 in tup)
print(max(tup))
print(min(tup))

fruits = ("Mango", "Liche", "banana")
for ft in fruits:
    print(ft)

print("lenth is: ", len(fruits))

print(tup.index(3))
print(tup.count(4))

""" two variable swaping in tuple"""
a, b = 10, 20
a,b = b,a
print(a,b)

nested = ((1,7), (2,3), (5,6))
"""
print(nested[1][0])
print(nested[2][1][0])
"""

print(sum(sum(t) for t in nested))



