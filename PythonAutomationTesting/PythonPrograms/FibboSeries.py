def fibbo(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, ", ")
        a, b=b, a+b

num = int(input("enter a number "))
fibbo(num)