def make_pizza(size, *toppings):
    """"brief introduce the pizza that you want to make"""
    print(f'\nMaking a {size}-inch pizza with the following toppings:')
    for topping in toppings:
        print(f"- {topping}")