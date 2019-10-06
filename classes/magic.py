import random


class Spell:

    def __init__(self, name, cost, dmg, typ3):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.typ3 = typ3

    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)
