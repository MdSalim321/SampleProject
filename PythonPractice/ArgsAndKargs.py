
print("_______Program with args______")
def Add(*args):
    sum = 0
    for num in args:
        sum = sum + num

    return sum

a = Add(10, 20, 30, 40)
print(a)

print("______Program with kwargs_______")

def userDetails(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

userDetails(name ="Bhai", age = 30, city = "Kolkata")

print("______Program with kwargs type2_______")

def detailsUser(*args, ** kwargs):
    print("args= ", args)
    print("kwargs= ",  kwargs)

detailsUser(1, 2, 3, name = "Bhai", age = 31, city = "Kolkata")

print("____Adding with args_______")
def addAll(*args):
    return sum(args)

print(addAll(12,23))

print("_____Anagram program_______")

