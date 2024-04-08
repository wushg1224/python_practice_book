from random import randint

class Die:
    ''''a try to create a die'''
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        ''''print  random sides'''
        print(f"you rolled {randint(1,self.sides)}")

pendan = Die(6)
pendan.roll_die()

ten_sides_die = Die(10)
ten_sides_die.roll_die()

ides_die = Die(20)
ides_die.roll_die()


