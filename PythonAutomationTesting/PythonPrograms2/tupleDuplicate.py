t = (1, 2, 3, 2, 4, 1)
duplicates = set([x for x in t if t.count(x) > 1])
print(duplicates)  # Output: {1, 2}
