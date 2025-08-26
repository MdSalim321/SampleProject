lst = [1,1,1,2,2,2,3,3,3,4,4]

removeDuplicates = set([x for x in lst if lst.count(x)> 1])
print(removeDuplicates)
