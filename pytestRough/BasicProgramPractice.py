class ReverseString:
    def __init__(self, str):
        rev = ""
        for char in str:
            rev = char + rev
        print(rev)

name = input("enter a string: ")
obj = ReverseString(name)
