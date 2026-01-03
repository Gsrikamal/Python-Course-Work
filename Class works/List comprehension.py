# List comprehension : short and clean way to create lists using a single line of code instead of long for loops.

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

result = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 6)]
print(result)

lc=[i for i in range(1,11)]
print(lc)

resl=[i for i in range(1,11) if i%2==0]
print(resl)

namesl=[input("enter the names:") for i in range(5)]
print(namesl)

s='python programming'
v='aeiouAEIOU'
r=[i if i in v else 0 for i in s]
print(r)

# set Comprehension: 

s='python programming language'
r=(i for i in s)
print(r)

# Tuple :

s='python programming language'
r=tuple(i for i in s)
print(r)

# dictionary :

d1={i:i*i for i in range(1,6)}
print(d1)

d1={input("enter the product:"): input("enter the price:") for i in range(1,6)}
print(d1) 



# ================================
# LIST COMPREHENSION IN PYTHON
# ================================

# 1. Basic List Comprehension
# Create a list of squares from 1 to 5
squares = [x * x for x in range(1, 6)]
print("Squares:", squares)


# 2. List Comprehension with condition (if)
# Get only even numbers from 1 to 10
evens = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers:", evens)


# 3. Convert string list to integer list
nums = ["1", "2", "3", "4"]
int_nums = [int(n) for n in nums]
print("Integer list:", int_nums)


# 4. Using if-else in list comprehension
# Label numbers as Even or Odd
even_odd = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 6)]
print("Even or Odd:", even_odd)


# 5. Working with strings
# Convert each character to uppercase
word = "python"
uppercase_chars = [ch.upper() for ch in word]
print("Uppercase characters:", uppercase_chars)


# 6. Nested List Comprehension (2D List / Matrix)
# Create a 3x3 matrix
matrix = [[j for j in range(3)] for i in range(3)]
print("Matrix:")
for row in matrix:
    print(row)


# 7. Flatten a 2D list into 1D list
matrix2 = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix2 for num in row]
print("Flattened list:", flattened)


# 8. Using function inside list comprehension
def square(n):
    return n * n

squared_values = [square(x) for x in range(1, 6)]
print("Squared using function:", squared_values)


# 9. Traditional for-loop vs List comprehension
# Normal method
traditional = []
for x in range(5):
    traditional.append(x * x)

# List comprehension method
comprehension = [x * x for x in range(5)]

print("Traditional:", traditional)
print("List Comprehension:", comprehension)


# 10. Filter words with length greater than 3
words = ["hi", "hello", "cat", "python", "go"]
long_words = [w for w in words if len(w) > 3]
print("Words length > 3:", long_words)


# 11. Get ASCII values of characters
chars = ['a', 'b', 'c']
ascii_values = [ord(c) for c in chars]
print("ASCII values:", ascii_values)


# 12. Square only positive numbers
numbers = [-4, -2, 0, 3, 5]
positive_squares = [x * x for x in numbers if x > 0]
print("Positive squares:", positive_squares)


# ================================
# END OF LIST COMPREHENSION EXAMPLES
# ================================
