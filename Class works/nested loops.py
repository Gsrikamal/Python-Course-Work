# Nested loops : 

for i in range(5):
    for j in range(5):
        print('*',end='    ')
    print()

for i in range(4):
    for j in range(5):
        print(j+1,end=' ')
    print()
    
for i in range(5):
    for j in range(6):
        print(i+1,end=' ')
    print()
   
# Left Side Pyramid  
rows=int(input("enter the size:"))
for i in range(1,rows+1):
    for j in range(i):
        print('*',end=" ")
    print()
   
# Reverse 
n=int(input("enter the size:"))
for i in range(n):
    for j in range(n-i):
        print("*",end=' ')
    print() 
    
# right side pyramid

n=int(input("enter the size:"))
for i in range(n):
    for space in range(n-1-i):
        print(" ",end=" ")
    for j in range(i+1):
        print('*',end=" ")
    print()

# Reverse

n=int(input("enter the size:"))
for i in range(n):
    for space in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print('*',end=" ")
    print()
    
# Hollow rectangle pattern
n=int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
    
# Z pattern 
n=int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()

# X patternms
n=int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(1,10,2):
    for j in range(1,100,5):
        print(i+j)

# 
n=int(input("enter the size:"))
for i in range(n):
    if i<=n//2:
        print('* '*(i+1))
    else:
        print('* '*(n-i))
        
# A 

n = int(input("Enter the size: "))

for row in range(n):
    for col in range(n):
        if row == 0 or col == 0 or col == n-1 or row == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

    
# G 
            
n = int(input("enter the size: "))
for row in range(n):
    for col in range(n):
        if (row == 0 or
            col == 0 or
            (row == n - 1 and col <= n // 20) or
            (col == n // 2 and row >= n // 2) or
            (row == n // 2 and col >= n // 2) or
            (col == n - 1 and row >= n // 2)):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
    
# 
n=int(input("enter the number:"))
sum=0
for i in range(1,n//2+1):
    if n%i==0:
        sum+=i
if sum==n:
    print("perfect number")
else:
    print("not a perfect number")