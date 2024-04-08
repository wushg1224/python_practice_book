number_of_reservation = input("How many people for your reservation? ")
number_of_reservation = int(number_of_reservation)

if number_of_reservation >= 8:
    print("sorry, no table")
else:
    print("Yes, we can book")