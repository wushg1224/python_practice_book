prompt = "\nTell me how old you are? I'll tell you your ticket price: "
prompt+= "Enter quit to end the program."

age=""

while age!='quit':
    age=input(prompt)
    if age != 'quit':
        age=int(age)
        if age<3:
            price=0
        elif age < 12:
            price=10
        else:
            price=15
        print(price)

