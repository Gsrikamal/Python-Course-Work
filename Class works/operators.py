# 1. Arithmetic Operators:

a = 10
b = 3

print(a + b)   # 13- addition
print(a - b)   # 7- subtraction
print(a * b)   # 30-    multiplication
print(a / b)   # 3.333- division
print(a % b)   # 1- modulus
print(a ** b)  # 1000 (10^3)- exponentiation
print(a // b)  # 3- floor division
# --------------------------------------------------------------------------------------

# 2. Assignment Operators:

x = 10
x += 5   # x = x + 5- addition assignment
print(x)  # 15

x -= 3
print(x)  # 12- subtraction assignment

x *= 2
print(x)  # 24- multiplication assignment

x /= 4
print(x)  # 6.0- division assignment
#---------------------------------------------------------------------------------------

# 3. Comparison (Relational) Operators:

a = 10
b = 20

print(a == b)  # False- equality
print(a != b)  # True-  inequality
print(a > b)   # False- greater than
print(a < b)   # True-     less than
print(a >= 10) # True- greater than or equal to
print(b <= 15) # False- less than or equal to
#---------------------------------------------------------------------------------------

# 4. Logical Operators: 
x = True
y = False   
print(x and y)  # False- logical AND    
print(x or y)   # True- logical OR
print(not x)    # False- logical NOT
#---------------------------------------------------------------------------------------

# 5. Bitwise Operators:
a = 5      # 0101 in binary
b = 3      # 0011 in binary 
print(a & b)  # 1  (0001)- bitwise AND
print(a | b)  # 7  (0111)-  bitwise OR
print(a ^ b)  # 6  (0110)- bitwise XOR
print(~a)     # -6 (inverts bits)- bitwise NOT
print(a << 1) # 10 (1010)- left shift
print(a >> 1) # 2  (0010)- right shift
#---------------------------------------------------------------------------------------

# 6. Membership Operators:
fruits = ["apple", "banana", "cherry"]  
print("banana" in fruits)      # True- membership test
print("grape" not in fruits)   # True-  non-membership test
#---------------------------------------------------------------------------------------

# 7. Identity Operators:

a = [1, 2, 3]
b = a
c = a.copy()
print(a is b)      # True- identity test
print(a is c)      # False- identity test
print(a == c)      # True- equality test
print(a is not c)  # True- identity test
#---------------------------------------------------------------------------------------

# 8. Operator Precedence:

result = 10 + 5 * 2  # Multiplication first
print(result)  # 20
result = (10 + 5) * 2  # Parentheses first
print(result)  # 30
#---------------------------------------------------------------------------------------

# 9. Ternary Operator:

age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Adult
#---------------------------------------------------------------------------------------