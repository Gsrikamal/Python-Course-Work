#1. Numeric Types

# int (integer)----Whole numbers (positive, negative)

a = 10
b = -5
print(type(a))  # <class 'int'>

#float (decimal)-----Numbers with decimal points
x = 10.5
y = -2.8
print(type(x))  # <class 'float'>

#complex (a + bj)------Numbers with real and imaginary parts
z = 2 + 3j
print(type(z))  # <class 'complex'>

# 2. String Type
# str------- Sequence of characters inside quotes.

name = "Subhash"
print(type(name))  # <class 'str'>

# 3. Sequence Types

# list----Ordered, changeable, allows duplicates.

my_list = [10, "apple", 2.5]
print(type(my_list))  # <class 'list'>

# tuple-----Ordered, unchangeable, allows duplicates.

my_tuple = (10, 20, 30)
print(type(my_tuple))  # <class 'tuple'>

# range-----Used for generating a sequence of numbers.

r = range(5)
print(list(r))  # [0, 1, 2, 3, 4]

#4. Mapping Types--- dict,Key–value pairs.

student = {"name": "Subhash", "age": 22}
print(type(student))  # <class 'dict'>

# 5. Set Types---set,Unordered, unique values.

s = {1, 2, 3, 2}
print(s)  # {1, 2, 3}

# frozenset-----Like set but unchangeable.

fs = frozenset([1, 2, 3])
print(type(fs))  # <class 'frozenset'>

# 6. Boolean Type--- bool,True / False

a = True
b = False
print(type(a))  # <class 'bool'>

# 7. Binary Types---Used for bytes and binary data,bytes
b = b"Hello"
print(type(b))  # <class 'bytes'>

# bytearray----Mutable bytes

ba = bytearray(5)
print(type(ba))  # <class 'bytearray'>

#memoryview

mv = memoryview(bytes(5))
print(type(mv))  # <class 'memoryview'>

# Special Type----- NoneType,Represents no value.

x = None
print(type(x))  # <class 'NoneType'>