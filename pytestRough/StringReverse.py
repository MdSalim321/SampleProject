class ReverseString:
    def __init__(self, str):
        rev= ""
        rev= str[::-1]
        print(rev)

        if str.lower()==rev.lower():
            print("Palindrome")
        else:
            print("Not Palindrome")

num = input("Enter a string:")
obj = ReverseString(num)


