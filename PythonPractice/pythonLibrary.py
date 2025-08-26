import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

result = np.dot(a, b)
print("Matrix Multiplication:\n", result)

arr = np.array([10, 20, 30, 40, 50])
print("Sliced [1:4]:", arr[1:4])

rand_arr = np.random.randint(1, 1000, size=(3, 3))
print("Random Array:\n", rand_arr)

arr = np.array([4, 1, 5, 2])
sorted_arr = np.sort(arr)
print("Sorted Array:", sorted_arr)

arr = np.array([[1, 2], [3, 4]])
flat = arr.flatten()
print("Flattened Array:", flat)

arr = np.array([1, 2, 2, 3, 4, 4, 5])
unique = np.unique(arr)
print("Unique Elements:", unique)

