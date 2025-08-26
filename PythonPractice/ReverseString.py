st = "Hello World"
print(st)
rev = st[::-1]
print(rev)

if st == rev:
    print("Palindrome ")
else:
    print("Not palindrome")

print("Reverse using for loop, after replacing the space")

revs = ""
st= st.replace(" ", "")
for ch in st:
    revs = ch+revs

print(revs)

if st == revs:
    print("Palindrome")
else:
    print("Not Palindrome")


print("Reverse using the join function")
print(" ".join(reversed(st)))

print("Vowel count & Consonent count")

st1 = "My name is Selim"
vowels = "aeiouAEIOU"

voCount = sum(1 for ch in st1 if ch in vowels)
print("Vowel count is:", voCount)
consCount = sum(1 for ch in st1 if ch.isalpha() and ch not in vowels)
print(consCount)





