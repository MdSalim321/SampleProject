st_arr = []

for i in range (5):
    name = input(f"input string is {i+1}:")
    st_arr.append(name)

print("You have entered: ", st_arr)

rev_st = st_arr[:: -1]

rev_st.count()
print("count is ", rev_st)

#st_arr.reverse()
print("Reverse array string is ", rev_st)
