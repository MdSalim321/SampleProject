print("each character occurance")
st = "Python language"
eachOcurance = {}
for ch in st:
    eachOcurance[ch] = eachOcurance.get(ch, 0)+1

print("Occurance of each character:\n ",eachOcurance)

print("Remove the duplicate character")
stt = "Python Programming language"
stt = stt.replace(" ", "")
print(stt)

result = "".join(sorted(set(stt), key=stt.index))
print(result)

print("First Non-repeted character")
str = "Python language"
for ch in str:
    if str.count(ch) == 2:
        print("First non-repetative character is: ", ch)
        break


print("_____Check the two String is Anagram or not______ ")
s1 = "Abcd"
s2 = "dcbae"
s1 = s1.lower()
s2 = s2.lower()
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

print("_____Print all the Substring_____")
s = "abc"
count = 0

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        print(s[i:j])
        count += 1

print("Total substring count is:", count)

print("_________convert the string into title case______")

s = "hello world from python"
print(s.title())

print("_________Reverse the words in the string______")

ss= "My name is, Mounia sharif."
words = ss.split()
print(words)
revWords = words[::-1]
print(revWords)
resultt = " ".join(revWords)
print(resultt)

print("_________Replace the word in a String______")

s3 = "I love India"
print(s3)
s3 = s3.replace("India", "Bharat")
print(s3)

print("_________String Contains numeric or not______")
s = "1222"
if s.isdigit():
    print("Numeric String")
else:
    print("Not Numeric")




