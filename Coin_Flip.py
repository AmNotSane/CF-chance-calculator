from random import choice


class HoT:
    def __init__(self, flips_amount, heads=0, tails=0):
        self.flips_amount = flips_amount
        self.heads = heads
        self.tails = tails

    def chance(self):
        option = ['H', 'T']
        for flips in range(self.flips_amount):
            result = choice(option)
            if result == option[0]:
                self.heads += 1
            elif result == option[1]:
                self.tails += 1

    def calculation(self):
        percentage_heads = self.heads * 100 // self.flips_amount
        percentage_tails = self.tails * 100 // self.flips_amount
        print('Heads : ' + str(self.heads) + ' with the chance of ' + str(percentage_heads) + '%')
        print('Tails : ' + str(self.tails) + ' with the chance of ' + str(percentage_tails) + '%')


def heads_tails():
    amount = int(input('How many flips? '))
    coin_flip = HoT(amount)
    coin_flip.chance()
    coin_flip.calculation()


heads_tails()
