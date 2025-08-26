for j in range(5):
    print(" " *(5-j), end="")
    print("*" *j)

for i in range(5, 0, -1):
    print("#" *i)

print("_____Pyramid pattern_______")
row = 5
for i in range(1, row+1):
    print(" "*(row -i) + "* "*i)

print("_____Dimomd Pattern_______")

rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)

print("__________Number Triangle_______")
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

print("__________Floyed Triangle_______")

rows = 5
num = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()

print("__________Right Aligned Triangle_______")

rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)

print("__________Alternatively 0 & 1 Triangle_______")

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print((i + j) % 2, end=' ')
    print()

print("__________Alphabet Pattern_______")


rows = 5
ascii_val = 65
for i in range(rows):
    for j in range(i + 1):
        print(chr(ascii_val), end=' ')
    ascii_val += 1
    print()

print("__________Hollo Square_______")


rows = 5
for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
