def anagram():
    st1 = "Listen"
    st2 = "Silent"
    st1 = st1.replace(" ", "").lower()
    st2 = st2.replace(" ", "").lower()

    b =sorted(st1) ==sorted(st2)
    if(b):
        print("Anagram")
    else:
        print("Not Anagram")

anagram()
