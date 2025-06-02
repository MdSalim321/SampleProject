st = input("Enter a string")
start = int(input("enter start index: "))
end = int(input("enter end index: "))

rst = st[:start]+st[start:end][::-1]+ st[end:]
print(rst)
