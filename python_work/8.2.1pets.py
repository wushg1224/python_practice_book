#order argument
def describe_pet(animal_type, pet_name):
    """"show pets information"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#keyword argument
def describe_pet(pet_name, animal_type='dog'):
    """"show pets info"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='jess')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='willie')

def describe_pet(pet_name, animal_type='dog'):
    """"show pets info"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet()