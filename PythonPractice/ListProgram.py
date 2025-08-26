import array as arr
numbers = arr.array('i', [10, 20, 30, 40, 50])
print("Array elements:", numbers)

print("List all operation")

numbers = [10, 80, 20, 90, 30]
print(numbers)
print("First numbers is: ",numbers[0])
print("Last numbers is: ", numbers[-1])
numbers.append(100)
print(numbers)
numbers.insert(6, 10)
print(numbers)
numbers.remove(100)
print(numbers)