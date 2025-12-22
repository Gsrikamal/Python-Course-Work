# input functions : enter values on screen or if user wants to enter input on screen then we use input functions.

# syntax : input("string")

a = input("Enter your name: ")
b = input("Enter your age: ") 
c=a+b
print(c)

# int(input())-----Converts input into an integer

age = int(input("Enter your age: "))
print(age + 5)

# float(input())--------Converts input into a decimal number

price = float(input("Enter price: "))
print(price)

# eval(input()) ⚠️ (Not Recommended)------Takes input as a Python expression

x = eval(input("Enter the input: "))
print(x, type(x))

# list of values as input
prices=list(map(float,input("Enter prices: ").split()))
print(prices)

# tuple of values as input
names = tuple(input("Enter names: ").split(","))
print(names)

# tuple of integers as input
inte=tuple(map(int,input("Enter integers: ").split(",")))
print(inte)

# tuple of prices as input
prices=tuple(map(float,input("Enter prices: ").split(',')))
print(prices)


# output function : to display output on screen we use print function.

# syntax : print(value1, value2, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
print("Hello", "World", sep="-", end="!!!\n")

print("Welcome to Python programming.")
# sep : specifies the separator between multiple values (default is space)