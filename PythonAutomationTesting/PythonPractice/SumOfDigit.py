class MySumOfDigit:
    def sumOfDigit(self, n):

        sum = 0
        while n>0:
            sum += n%10
            n //=10

        return sum

n = int(input("Enter a number: "))
m = n
obj = MySumOfDigit()
sum = obj.sumOfDigit(n)
print(f"Sum of the digit for the number {m} is -", sum)


