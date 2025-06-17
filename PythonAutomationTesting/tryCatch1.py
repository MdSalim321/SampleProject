
try:
    num = int(input("enter a number"))
    res = 10/num

except ZeroDivisionError as z:
    print("not divisible by zero")

except ValueError as v:
    print("this is not a valid input")

else:
    print(f"result is: {res}")


finally:
    print("This code will execute always")