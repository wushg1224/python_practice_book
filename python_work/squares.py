squares=[]
for value in range(1,10):
    square=value**2
    squares.append(square)
print(squares)

for value in range(1,11):
    squares.append(value**2)
print(squares)


squares=[value**2 for value in range(1,11)]
print(squares)