lst = ["Apple", "Banana","Banana", "Cherry"]
print(lst)

print(len(lst))
print(lst[1])
print(type(lst))

list = ["Apple", 1, True, "Banana"]
print(list)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[0:5])

thislist[1] = "Begun"
print(thislist)

thislist[0:3] = ["Vajji", "Alu"]
print(thislist)

#thislist[0:7] = ["Sample"]
#print(thislist)

thislist.insert(2, "Spoon")
print(thislist)

thislist.append("Mango")
print(thislist)

tropics = ["equatorial", "tropical", "Subtropical"]
thislist.extend(tropics)
print(thislist)

thislist.remove("tropical")
print(thislist)

thislist.pop(1)
print(thislist)






