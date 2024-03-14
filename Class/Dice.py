from random import randint as ran


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        tries = 0
        while True:
            num1 = ran(1, self.sides)
            num2 = ran(1, self.sides)
            print(num1, '--', num2)
            tries += 1
            if tries == 10:
                break


ft = Die(3)
ft.roll_die()
