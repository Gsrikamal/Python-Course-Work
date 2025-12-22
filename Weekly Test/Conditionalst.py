# PYTHON WEEKLY TEST – 2
# Topic: Conditional Statements

# ---------------- Q1 ----------------
# Even or Odd Checker
n = int(input())
if n % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# ---------------- Q2 ----------------
# Positive, Negative or Zero
n = int(input())
if n > 0:
    print("Positive Number")
elif n < 0:
    print("Negative Number")
else:
    print("Zero")


# ---------------- Q3 ----------------
# Voting Eligibility Check
age = int(input())
if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")


# ---------------- Q4 ----------------
# Largest of Two Numbers
a = int(input())
b = int(input())
if a > b:
    print(a)
else:
    print(b)


# ---------------- Q5 ----------------
# Largest of Three Numbers (NESTED IF)
a = int(input())
b = int(input())
c = int(input())

if a >= b:
    if a >= c:
        print(a)
    else:
        print(c)
else:
    if b >= c:
        print(b)
    else:
        print(c)


# ---------------- Q6 ----------------
# Grade Calculator
marks = int(input())
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")


# ---------------- Q7 ----------------
# Login Validation
username = input()
password = input()

if username == "admin" and password == "1234":
    print("Login Successful")
elif username == "admin":
    print("Invalid Password")
else:
    print("Invalid Username")


# ---------------- Q8 ----------------
# Number Range Checker
n = int(input())
if 1 <= n <= 10:
    print("Between 1 and 10")
elif 11 <= n <= 20:
    print("Between 11 and 20")
else:
    print("Greater than 20")


# ---------------- Q9 ----------------
# Simple Calculator
a = int(input())
b = int(input())
op = input()

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid Operator")


# ---------------- Q10 ----------------
# Pass or Fail Checker
marks = int(input())
if marks >= 40:
    print("Pass")
else:
    print("Fail")
