# =========================================
# Python Weekly Test – 4
# Name: G. S. Kamal
# =========================================


# Q1. Basic Loop
# Write a Python program to print numbers from 1 to n in a single line separated by space.

n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(i, end=" ")
print("\n")


# Q2. Right Angle Number Triangle
# Write a Python program to print a right-angled number triangle using nested loops.

rows = int(input("Enter rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
print()


# Q3. Inverted Star Pattern
# Write a Python program to print an inverted star pattern using nested loops.

rows = int(input("Enter rows: "))
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
print()


# Q4. Multiplication Tables
# Write a Python program to display multiplication tables from 1 to n using nested loops.

n = int(input("Enter number: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i} x {j} = {i*j}")
    print()


# Q5. Pyramid Star Pattern
# Write a Python program to print a pyramid star pattern using nested loops.

rows = int(input("Enter rows: "))
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2*i - 1))
print()


# Q6. List Comprehension – Even Numbers
# Write a Python program to generate a list of even numbers from 1 to n using list comprehension.

n = int(input("Enter n: "))
even_numbers = [i for i in range(1, n + 1) if i % 2 == 0]
print(even_numbers)
print()


# Q7. List Comprehension – Squares of Odd Numbers
# Write a Python program to create a list containing squares of odd numbers between 1 and n.

n = int(input("Enter n: "))
odd_squares = [i*i for i in range(1, n + 1) if i % 2 != 0]
print(odd_squares)
print()


# Q8. Tough – Conditional Pattern (Nested Loops)
# Write a Python program to print a pattern where the row number is printed at odd positions
# and '*' is printed at even positions using nested loops.

rows = int(input("Enter rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j % 2 != 0:
            print(i, end="")
        else:
            print("*", end="")
    print()
print()


# Q9. List Comprehension – Word Filter
# Write a Python program to filter and display words whose length is greater than 3 using list comprehension.

words = input("Enter words: ").split()
filtered_words = [word for word in words if len(word) > 3]
print(filtered_words)
print()


# Q10. Floyd’s Triangle
# Write a Python program to print Floyd’s Triangle using nested loops.

rows = int(input("Enter rows: "))
num = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
