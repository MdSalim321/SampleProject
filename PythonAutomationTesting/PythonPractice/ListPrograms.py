lst = [20, 30, 50, 10, 60]
print(lst)

print(sorted(lst))
print(max(lst))
print(min(lst))
print(sum(lst))
print(lst[1])

print(lst[:2])
print(lst[2:])
print(lst[::-1])

for i in lst:
    print(i)

lst.append(100)
print(lst)
lst.insert(0, 200)
print(lst)

lst.remove(100)
print(lst)
del lst[0]
print(lst)

