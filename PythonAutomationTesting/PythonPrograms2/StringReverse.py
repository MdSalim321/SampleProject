st = input("Enter a string: ")
print(st)
"""
rst = st[::-1]
print(rst)
"""

rst = " "
for char in st:
    rst= char+ rst
print(f"reverse string is of {st} is: ", rst)

print("Reverse in another way")
for i in range(len(st)-1, -1, -1):
    rst = rst+st[i]

print(f"reverse string is of {st} is: ", rst)







