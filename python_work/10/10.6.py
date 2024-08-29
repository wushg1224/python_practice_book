# calculator

print("Give me two numbers, and I'll add them up.")
print("ENTER 'q' to quit.")

first_number = input("\nFirst number:")
if first_number == 'q':
    print("Goodbye")
    exit()
second_number = input("Second number: ")
if second_number == 'q':
    print("Goodbye")
    exit()
try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print('you must enter a number')
else:
    print(answer)
