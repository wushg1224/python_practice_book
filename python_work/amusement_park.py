age=12

if age<4:
    print("Your admissioin cost is $0")
elif age<18:
    print("Your admissioin cost is $25")
else:
    print("Your admissioin cost is $40")

age=12

if age<4:
    price=0
elif age<18:
    price=25
else:
    price=40
print(f"Your admjission cost is ${price}")

if age<4:
    price=0
elif age<18:
    price=25
elif age<65:
    price=40
else:
    price=20
print(f"Your admjission cost is ${price}")