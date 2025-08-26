from itertools import count

print("_______List Operation________")

lst = [10, 60, 30, 40, 50, True, "Apple"]
print(lst)
lst.append("Banana")
print(lst)
print(lst[1])
lst[0]= 99
print(lst)

print(type(lst))
print(lst[0:5])

print("________Tuple Operation_________")
myTuple = (1,2,3, "Bhai", False)
print(myTuple)
print(myTuple[4])
print(myTuple[0:3])

print("________Range Operation_________")
myrange = range(10)
print(myrange)
print(list(myrange))
print(tuple(myrange))
print(set(myrange))

print(list(range(0,100,5)))
num = list(range(0,100,5))
print(len(num))

print("________List Operation_________")
square = [x**3 for x in range(1,100)]
print(square)

















