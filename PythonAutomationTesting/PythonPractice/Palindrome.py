class MyPalindrome:
    def PalinfromeCheck(self):
        st = "SelimileS"
        st2 = st.lower()
        print(st2)
        st1 = st2[::-1]
        if st1 == st2:
            print("Palindrome")
        else:
            print("Not a Palindrome")

obj = MyPalindrome()
obj.PalinfromeCheck()