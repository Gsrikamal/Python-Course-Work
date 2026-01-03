# they help repeat a block of code multiple times until a certain condition is met.
# In Python, the main looping control statements are 'for' loops and 'while' loops.


# 1. For Loop : A 'for' loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string).

# list of fruits :

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
# tuple of numbers :

numbers = (1, 2, 3, 4, 5)
for i in numbers:
    print(i)
    
# dictionary of products :

products = {"laptop": 1000, "phone": 500, "tablet": 300}
for product in products:
    print(product, products[product])
    

# set of colors :

colors = {"red", "green", "blue"}
for i in colors:
    print(i)


# 2. While Loop : A 'while' loop repeatedly executes a block of code as long as a specified condition is true.

count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # Increment the count to avoid infinite loop

# 3. Break Statement : The 'break' statement is used to exit a loop prematurely when a certain condition is met.    

for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)
    
 # or # 
 
list=[1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in list:
    if i > 6:
        break  # Exit the loop when num is greater than 6
    print(i)

# 4. Continue Statement : The 'continue' statement is used to skip the current iteration of a loop and move to the next iteration.

for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # This will print only odd numbers

# or # 

list=[1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in list:
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # This will print only odd numbers    
    
# 5.pass Statement : The 'pass' statement is a placeholder that does nothing. It is used when a statement is syntactically required but no action is needed.

for i in range(5):
    if i == 3:
        pass  # Placeholder for future code
    print(i)
    
 # or #
 
list=[1, 2, 3, 4, 5]
for i in list:
    if i == 3:
        pass  # Placeholder for future code
    print(i)