pizzas=['margarita','hawaii','vegan','napolitana','pepperoni']
for pizza in pizzas:
    print(f'I Like {pizza} pizza!\n')
print("I really love pizza!")

friends_pizzas=pizzas[:]
friends_pizzas.append("榴莲披萨")

print(f'my favorite pizzas are {pizzas}!')
print(f"my friend's favorite pizzas are{friends_pizzas}!")

for friends_pizza in friends_pizzas:
    print("my friends's favotire pizzas are:")
    print(friends_pizza)

pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese'],
    }
print(f"You ordered a {pizza['crust']}-crust pizza"
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f'\t{topping}')