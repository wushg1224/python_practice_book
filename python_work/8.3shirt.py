def make_shirt(size, txt):
    """"accept size and pattern show on t-shirt"""
    print(f"/nThe shirt size is{size}.")
    print(f"The required pattern is {txt}.")

make_shirt(8, '无印良品')

def make_shirt(size, txt='I love Python'):
    """"accept size and pattern show on t-shirt"""
    print(f"\nThe shirt size is {size}.")
    print(f"The required pattern is {txt}.")

make_shirt('small')
make_shirt('medium')