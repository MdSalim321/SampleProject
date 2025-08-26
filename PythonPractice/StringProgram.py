from openpyxl.descriptors import String

word = "Programming"
character = 'g'
count =0
for i_k in word:
    if i_k == character:
        count +=1
print(count)

print("___________________")
fibbo = [0, 1]
n= 10
for i in range(n):
    fibbo.append(fibbo[-1] + fibbo[-2])

print(", ".join(str(k) for k in fibbo))

print("___________________")
myList = [65, 23, 67, 98, 6, 88]
max = myList[0]
for num in myList:
    if max < num:
        max = num

print(max)

print("___________________")

mlist = ["P", "Y", "T", "H", "O", "N"]
string = "".join(mlist)
print(string)
print("___________________")
list1 = [23,45,56]
list2 = [12,23,45]
lst = []
for i in range(0, len(list1)):
    lst.append(list1[i]+list2[i])

print(lst)

print("___________________")
str1 = "listent"
str2 = "Silent"
str1 = str1.replace(" ", "").upper()
str2 = str2.replace(" ","").upper()

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print(" Not Anagram")

print("___________________")

strr1 = "Abcba"
strr2 = strr1.lower()
if strr2 == strr2[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

print("___________________")
st = "Pro  Gra  mm  ing"
print(st.count(" "))

print("_________Count Special character__________")

str = "asdfrtyuuh$%^&*IOO&*()"
spChar = "!@#$%^&*()<>?,./;:'[]{}"
count = 0
for i in str:
    if i in spChar:
        count+=1
print(f"the number of Special character in {str} is: ", count)

print("______ Removing the white Space____")
stt = " Pro  gramm  ing"
st2= stt.replace(" ", "")
print(st2)

