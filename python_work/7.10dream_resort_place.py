resorts= {}

question_active = True

while question_active:
    name = input ('What is your name? ')
    place = input ('If you could visit one place in the world, where would you go?  ')

    resorts[name] = place
    
    repeat = input("Would you like to let another person respond? (Yes/ no) ")
    if repeat == "no":
        question_active_active= False
        print("\n ----qustion results---")
        for name, place in resorts.items():
            print(f"{name} would like to visit {place}.")

