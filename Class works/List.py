# Creating a list
fruits = ["apple", "banana", "mango"]
print("Fruits:", fruits)

# Nested list
nested = [1, 2, ["a", "b", "c"]]
print("Nested list:", nested)

# Adding items
fruits.append("orange")  # add at end
fruits.insert(1, "grapes")  # add at index
print("Updated Fruits:", fruits)

# Accessing items
print("First item:", fruits[0])
print("Last item:", fruits[-1])

# Basic List Methods in Python

#append() – adds an item to the end of the list
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)    # [1, 2, 3, 4]        

# insert() – adds item at a specific index
numbers = [10, 20, 30]
numbers.insert(1, 15)
print(numbers)  # [10,15, 20, 30]   

# extend() – add multiple items
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)  # [1, 2, 3, 4]         

#remove() – removes the first matching item
fruits = ["apple", "banana", "apple"]
fruits.remove("apple")
print(fruits)  # ['banana', 'apple']

#pop() – removes and returns an item
numbers = [10, 20, 30]
x = numbers.pop(1)
print(x)         # 20
print(numbers)   # [10, 30]

#clear() – removes all items
items = [1, 2, 3]
items.clear()
print(items)  # []

# count() – counts how many times an item appears
a = [1, 2, 1, 3, 1]
print(a.count(1))  # 3

#index() – returns index of item
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))  # 1

#sort() – sorts in ascending order
nums = [5, 2, 9, 1]
nums.sort()
print(nums)  # [1, 2, 5, 9]

#reverse() – reverses the list
nums = [1, 2, 3]
nums.reverse()
print(nums)  # [3, 2, 1]

# copy() – returns a copy of the list
a = [1, 2, 3]
b = a.copy()
print(b)  # [1, 2, 3]

# Extra Useful Operations (Not methods)

# Length of list
a = [10, 20, 30]
print(len(a))  # 3

#Slicing
a = [10, 20, 30, 40, 50]
print(a[1:4])  # [20, 30, 40]