try:
    result = 10/0
    print("this will not print")

except ZeroDivisionError:
    print("U can not divide by zero")


try:
    num = int('abc')

#except ValueError:
   # print("could not convert to integer")

except ValueError:
    print("not divisible by zero")

