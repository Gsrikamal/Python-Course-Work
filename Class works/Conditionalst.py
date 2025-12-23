# Conditional statements :
# execites a block of code if a specified condition is true.
# if condition :  

# 1. simple if statement :  code to be executed if condition is true

age = 20
if age >= 18:
    print("Eligible to vote")   
if age>=25:
    print("marriage")

# or 

age = int(input("enter your age:"))
if age >= 18:
    print("Eligible to vote")   
if age>=25:
    print("marriage")
if age>=30:
    print("childerns age")
if age<18:
    print("minior")

# 2. if-else statement : code to be executed if condition is true, else code to be executed if condition is false

num = 5
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
    
# or 

age = 20
if age >=18:
    print("Eligible to vote")
else:
    print("miner")
    

# 3. if-elif-else statement : code to be executed if first condition is true, else if second condition is true, else code to be executed if both conditions are false

age= 100
if age<= 90:
    print("Eligible for vote")    
elif age<= 200:
    print("Eligible foe driving license")
else:
    print("Eligible for marriage")
    
# or 

amount=int(input("enter a amount:"))
if amount>10000:
    print("trip to himalaya")
elif 8000<= amount<10000:
    print("trip to delhi")
elif 5000<= amount<8000:
    print("trip to benguluru")
else:
    print("trip to hyd")
    
    
# 4. nested if statement : an if statement inside another if statement

num = 10
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
        
# 0r 

age = int(input("enter your age:"))
if age >= 30:
    print("children's age")
else:
    if age >= 25:
        print("marriage")
    else:
        if age >= 18:
            print("Eligible to vote")
        else:
            print("minor")

        
            



 