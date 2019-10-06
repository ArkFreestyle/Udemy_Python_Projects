import random
from .magic import Spell


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_max_mp(self):
        return self.max_mp

    def get_mp(self):
        return self.mp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n" + BColors.BOLD + self.name + BColors.ENDC)
        print(BColors.OKBLUE + "\tACTIONS" + BColors.ENDC)
        for item in self.actions:
            print("\t\t" + str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + BColors.OKBLUE + "\tMAGIC", BColors.ENDC)
        for spell in self.magic:
            print("\t\t" + str(i) + ".", spell.name, "cost:", str(spell.cost))
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + BColors.OKGREEN + "\tITEMS" + BColors.ENDC)
        for item in self.items:
            print("\t\t" + str(i) + ".", item['item'].name, ":", item['item'].description + " x" + str(item['quantity']))
            i += 1

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def get_stats(self):

        hp_bar = ""
        bar_ticks = (self.hp / self.max_hp) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.max_mp) * 100 / 10
        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""
        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.max_mp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)
            while decreased > 0:
                current_mp += " "
                decreased -= 1
            current_mp += mp_string
        else:
            current_mp = mp_string
        print("                   -----------------------------        ------------")
        print(BColors.BOLD + self.name + "   " +
                             current_hp + BColors.OKGREEN
              + "   " + " |" + hp_bar + "|" + BColors.ENDC + " " + BColors.BOLD +
              current_mp + " " + BColors.OKBLUE + "|" + mp_bar + "|" + BColors.ENDC)

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.max_hp) * 100 / 2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""
        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                   ------------------------------------------------------")
        print(BColors.BOLD + self.name + "" +
              current_hp + BColors.WARNING
              + "  " + " |" + hp_bar + "|" + BColors.ENDC + " ")

    def choose_target(self, enemies):

        print("\n" + BColors.WARNING + BColors.BOLD
              + "    TARGET:" + BColors.ENDC)
        for counter, enemy in enumerate(enemies):
            if enemy.get_hp() != 0:
                print("      " + str(counter) + ".", enemy.name)

        choice = int(input("    Choose target:"))

        return choice

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        if spell.typ3 == "white":
            print("Okay the enemy chose a white spell")
            print("Enemy's hp:", self.hp)
            print("Enemy's max hp:", self.max_hp)
            print("Enemy's hp %:", (self.hp/self.max_hp)*100)

        if spell.typ3 == "white" and (self.hp / self.max_hp) * 100 > 50:
            print("I came inside the if statement! unfffffffffff")
            return self.choose_enemy_spell()
            print("I'm on the next line lmao, ignored the recursion lolol")
        if self.mp < spell.cost:
            spell = "No MP"
            magic_dmg = 0
            return spell, magic_dmg
        else:
            return spell, magic_dmg
