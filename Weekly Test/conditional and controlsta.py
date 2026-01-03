# Automated Salary tax Calculator

salary = float(input())

if salary <= 250000:
    tax = 0.0
elif salary <= 500000:
    tax = salary * 0.05
elif salary <= 1000000:
    tax = salary * 0.20
else:
    tax = salary * 0.30

print(float(tax))

# Movie Ticket Pricing Sysytem

n = int(input())
total = 0

for _ in range(n):
    age = int(input())
    if age < 5:
        price = 0
    elif age <= 18:
        price = 100
    elif age <= 60:
        price = 150
    else:
        price = 120
    total += price

print(total)


#  Electricity Bill Generator

units = int(input())
bill = 0.0

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = (100 * 1.5) + (units - 100) * 2.5
elif units <= 500:
    bill = (100 * 1.5) + (100 * 2.5) + (units - 200) * 4
else:
    bill = (100 * 1.5) + (100 * 2.5) + (300 * 4) + (units - 500) * 6

print(float(bill))

# Car Parking Fee Calculator

hours = int(input())

if hours <= 2:
    fee = 30
else:
    fee = 30 + (hours - 2) * 10

if fee > 200:
    fee = 200

print(fee)

# Product Inventory Checker(Nested Conditionals)

product = input()
quantity = int(input())

if quantity == 0:
    status = "Out of Stock"
elif quantity <= 10:
    status = "Low Stock"
elif quantity <= 50:
    status = "In Stock"
else:
    status = "Overstocked"

print(f"{product}: {status}")

# Prime Numbers Checker

n=int(input())
for i in range(2,n//2+1):
    if n%i==0:
        print("not prime number")
    break
else:
    print("not prime number")

# Gym Subscription Billing (Menu Driven Program)

choice = int(input())
people = int(input())

if choice == 1:
    cost = 1500
elif choice == 2:
    cost = 1300
elif choice == 3:
    cost = 5000
else:
    cost = 0

print(cost * people)

# Billing Bot –Apply Discount Based on Amount

amount = float(input())

if amount < 1000:
    discount = 0
elif amount < 5000:
    discount = 0.05
elif amount < 10000:
    discount = 0.10
else:
    discount = 0.15

final_amount = amount - (amount * discount)
print(float(final_amount))

# ATM PIN Verfication with Blocking Logic 

correct_pin = "1234"
attempts = 0
access = False

while attempts < 3:
    pin = input()
    attempts += 1
    if pin == correct_pin:
        access = True
        break

if access:
    print("Access Granted")
else:
    print("ATM Blocked. Try Again Later.")

# Bus Booking System-Track full and Empty Seats

total_seats = int(input())
booked_list = list(map(int, input().split()))

booked = len(booked_list)
available = total_seats - booked

print("Total Seats:", total_seats)
print("Booked:", booked)
print("Available:", available)