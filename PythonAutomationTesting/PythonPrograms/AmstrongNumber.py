n= int(input("Enter e number to checkout, it is amstrong number or not"))
num = n
sumCubes =0
while n> 0:
    r= n%10
    sumCubes += r ** 3
    n //= 10
print(sumCubes == num)
