n=int(input("Enter a number: "))
SumOfDigit =0

while n >0:
    r = n%10
    SumOfDigit = SumOfDigit + r
    n //=10

print(SumOfDigit)

