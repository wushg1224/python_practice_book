#calculator

print("Give me two numbers, and I'll add them up.")
print("ENTER 'q' to quit.")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        print("Goodbye")
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        print("Goodbye")
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        pass
    else:
        print(answer)