def make_pizza(*toppings):
    ''''打印顾客点的所有配料'''
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushroom', 'green pepper', 'extra cheese')


def make_milktea(size, *toppings):
    """"概述要制作的奶茶"""
    print(f"\nMaking a{size}milktea with the following toppings:")
    for topping in toppings:
        print(f"{topping}")

make_milktea('大杯','珍珠')
make_milktea('中杯','奶盖',"椰果", "布丁")