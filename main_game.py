"""Simple Final Fantasy inspired text based game implementation following a Udemy course instructor"""

from classes.game import Person, BColors
from classes.magic import Spell
from classes.inventory import Item
import random

# print("                   -------------------------       ----------")
# print(BColors.BOLD + "ARK:   "
#                      "460/460 |" + BColors.OKGREEN + "  |████████████████████████ |" +
#       BColors.OKBLUE + "     |██████████|")
# print("                   -------------------------       ----------")
# print(BColors.BOLD + "ARK:   "
#                      "460/460 |" + BColors.OKGREEN + "  |████████████████████████ |" +
#       BColors.OKBLUE + "     |██████████|")
# print("                   -------------------------       ----------")
# print(BColors.BOLD + "ARK:   "
#                      "460/460 |" + BColors.OKGREEN + "  |████████████████████████ |" +
#       BColors.OKBLUE + "     |██████████|")

# Create some black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 120, "black")
blizzard = Spell("Blizzard", 10, 110, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create some white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
hielixir = Item("MegaElixir", "elixir", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
enemy_spells = [fire, meteor, cure]
player_items = [{"item": potion, "quantity": 5},
                {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},
                {"item": elixir, "quantity": 5},
                {"item": hielixir, "quantity": 5},
                {"item": grenade, "quantity": 5}]

# Instantiate player and enemy
player1 = Person("ARK:", 700, 65, 60, 43, player_spells, player_items)
player2 = Person("MFK:", 460, 65, 60, 43, player_spells, player_items)
player3 = Person("M&M:", 460, 65, 60, 43, player_spells, player_items)

players = [player1, player2, player3]

enemy1 = Person("Minion", 400, 300, 40, 300, enemy_spells, [])
enemy2 = Person("CthuLu", 9999, 1000, 300, 25, enemy_spells, [])
enemy3 = Person("Neesan", 710, 400, 40, 100, enemy_spells, [])

enemies = [enemy1, enemy2, enemy3]
running = True
i = 0

print("\n\n")
print(BColors.FAIL + BColors.BOLD + "AN ENEMY ATTACKS!" + BColors.ENDC)

while running:
    print("=============================================")
    print("\n\n")
    print("NAME               HP                                MP")
    for player in players:
        player.get_stats()

    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:

        player.choose_action()
        choice = input("\nChoose action: ")
        choice = int(choice) - 1

        if choice == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("You attacked", enemies[enemy].name, "for", dmg, "points of damage.")

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + " has died.")
                del enemies[enemy]

        elif choice == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic: ")) - 1

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()
            if spell.cost > current_mp:
                print(BColors.FAIL + "\nNot enough MP\n" + BColors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.typ3 == "white":
                player.heal(magic_dmg)
                print(BColors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + BColors.ENDC)

            elif spell.typ3 == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(BColors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to "
                      + enemies[enemy].name + BColors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died.")
                    del enemies[enemy]

        elif choice == 2:
            player.choose_item()
            item_choice = int(input("Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(BColors.FAIL + "\n" + "None left..." + BColors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.typ3 == "potion":
                player.heal(item.prop)
                print(BColors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + BColors.ENDC)
            if item.typ3 == "elixir":
                player.hp = player.max_hp
                player.mp = player.max_mp
                print(BColors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + BColors.ENDC)
            elif item.typ3 == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(BColors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage to "
                      + enemies[enemy].name + BColors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died.")
                    del enemies[enemy]

    # Check if battle is over
    defeated_enemies = 0
    defeated_players = 0
    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    # Check if player won
    if defeated_enemies == 2:
        print(BColors.OKGREEN + "You win!" + BColors.ENDC)
        running = False

    # Check if enemy won
    elif defeated_players == 2:
        print(BColors.FAIL + "Your enemies have defeated you!" + BColors.FAIL)
        running = False

    print("\n")
    # Enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)
        # Choose who to attack
        target = random.randrange(0, 3)

        if enemy_choice == 0:
            enemy_dmg = enemy.generate_damage()
            players[target].take_damage(enemy_dmg)
            print(enemy.name.replace(":", ""), "attacks", players[target].name.replace(":", ""), "for", enemy_dmg, "points of damage.")
            if players[target].get_hp() == 0:
                print(players[target].name + " has died.")
                #del players[target]
        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()

            if spell == "No MP" and magic_dmg == 0:
                enemy_dmg = enemy.generate_damage()
                players[target].take_damage(enemy_dmg)
                print(enemy.name.replace(":", ""), "attacks", players[target].name.replace(":", ""), "for", enemy_dmg,
                      "points of damage.")
            else:
                enemy.reduce_mp(spell.cost)

                if spell.typ3 == "white":
                    enemy.heal(magic_dmg)
                    print(BColors.WARNING + spell.name + " heals", enemy.name, "for", str(magic_dmg), "HP." + BColors.ENDC)

                elif spell.typ3 == "black":

                    players[target].take_damage(spell.dmg)
                    print(BColors.FAIL + enemy.name.replace(":", "") + " used " + spell.name + " which deals", str(magic_dmg), "points of damage to "
                          + players[target].name.replace(":", "") + BColors.ENDC)
                    if players[target].get_hp() == 0:
                        print(players[target].name + " has died.")
                        #del players[target]


    print("-----------------------------------------")
    print("\nEnemy HP:", BColors.FAIL + str(enemies[0].get_hp()) + "/" + str(enemies[0].get_max_hp()) + BColors.ENDC)
