requested_topping='mushroom'
if requested_topping !='anchovies':
    print('Hold the anchovies!')

requested_toppings=["mushroom","extra cheese"]
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")



requested_toppings=["mushroom","extra cheese",'green peppers']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("sorry, we are out of green peppers right now.")
    else:
        print(f'Adding {requested_topping}.')
print("\nFinished making your pizza!")


requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}.')
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a paiin pizza?")

available_toppings=["mushroom","extra cheese",'green peppers','olives',
                    'pineapple','peperoni']
requested_toppings=["mushroom","extra cheese",'french fries']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}')
    else:
        print(f'Sorry, we doont have {requested_topping}.')
print('\nFinished making your pizza!')
        
