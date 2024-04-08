favorite_number={}
favorite_number['joyce']= 4
favorite_number['cecilia'] = 24
favorite_number['bowen'] = 8
favorite_number ['nini'] = 11
favorite_number ['shel'] = 12
print(favorite_number)

favorite_number={}
favorite_number['joyce']= 4 , 12 , 24 ,
favorite_number['cecilia'] = 24, 33 , 34 ,
favorite_number['bowen'] = 8, 15,
favorite_number ['nini'] = 11, 3
favorite_number ['shel'] = 12, 4
print(favorite_number)

for name, numbers in favorite_number.items
():
    print(f"{name.title()}'s favorite number are:{numbers}")