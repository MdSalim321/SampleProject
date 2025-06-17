try:
    resu = 2 + 'num'
except TypeError:
    print("this is type mismatch")

try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Index out of range!")

try:
    my_dict = {"name": "Alice"}
    print(my_dict["age"])
except KeyError:
    print("Key not found in dictionary!")


try:
    x = 5
    x.append(2)
except AttributeError:
    print("Attribute not found!")


try:
    with open("./DataSet.DataSheet.xlsx", "r") as f:
        content = f.read()
        print("file read")
except FileNotFoundError:
    print("File not found!")

try:
    import non_existing_module
except ImportError:
    print("Module not found!")

try:
    print(undeclared_variable)
except NameError:
    print("Variable is not defined!")


try:
    a = 'a' * (10**12)
except MemoryError:
    print("Out of memory!")
