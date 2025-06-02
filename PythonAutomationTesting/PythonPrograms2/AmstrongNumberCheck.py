num = int(input("Enter a number"))
n= num
sum = 0
while num > 0:
    r= num % 10;
    sum += r**3
    num //= 10

if sum ==n:
    print(f"{n} is a amstrong number")
else:
    print(f"{n} is not a amstrong number")






