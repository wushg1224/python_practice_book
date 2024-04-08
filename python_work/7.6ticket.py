prompt = "\nTell me how old you are? I'll tell you your ticket price: "
prompt+= "Enter quit to end the program."

while True:
    age=input(prompt)
    age=int(age)
    if age<3:
        price=0
    elif age < 12:
        price=10
    else:
        price=15
    
    if age=='quit':
        break
    else:
        print(price)