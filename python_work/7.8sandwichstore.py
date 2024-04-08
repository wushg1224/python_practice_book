sandwich_orders =['chicken sandwich','beef sandwich',
                  'pastrami sandwich','blt sandwich',
                  'ham sandwich','pastrami sandwich',
                  'cheese sandwich','pastrami sandwich',]
finished_sandwiches=[]

print("Pastrami Sandwich sold out")
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
    
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"\nI made your {current_sandwich.title()}!")
    finished_sandwiches.append(current_sandwich)

print(f"\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
