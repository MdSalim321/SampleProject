def factorials (num):
    if num == 0:
        return 1
    else:
        return num * factorials(num-1)

num = int(input("Enter a number, whoes factorial you want to findout"))
fact = factorials(num)
print(f"the factorial of number {num} is {fact}")