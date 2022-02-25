
from rpg_battle import *

from rpg_town import *

from rpg_functions import type_print

barbarian = Barbarian(race = "human")
medic = Medic(race = "human")
rogue = Rogue(race = "human")

# store = [Helper.SuperTonic]

# store_description = {
#     "Super Tonic": "A tonic that restores 10 HP. Can be used in battle."
#     }



def main(player):
    type_print(f"\nWith only {player.coin_purse} gold to your name, you head into town to find some work.\n")
    town(player)
    while True:
        type_print("What do you want to do?\n")
        type_print("1. Fight your bounty")
        type_print("2. Go to town")
        type_print("3. View current bounty")
        type_print("4. View inventory")
        type_print("5. View status")
        type_print("6. Pay off debt.")
        type_print("7. Quit")
        # type_print("3. Explore.")
        print("> ", end = ' ')
        raw_input = input()
        print("________________________________________________________________________________________________\n")
        if raw_input == "1":
            # choose enemy function
            if player.current_bounty == []:
                type_print("You currently don't have a bounty. Be sure to check the bounty board in town to grab one.\n ")
            else:
                battle(player, player.current_bounty[0])
        elif raw_input == "2":
            town(player)
        elif raw_input == "3":
            if player.current_bounty == []:
                type_print("You currently don't have a bounty. Be sure to check the bounty board in town to grab one.\n ")
            else:
                type_print(f"You current bounty is {player.current_bounty[0].name} ({player.current_bounty[0].race}) - {player.current_bounty[0].bounty} gold.\n")
        elif raw_input == "4":
            check_inventory(player)
        elif raw_input == "5":
            player.print_status()
        elif raw_input == "6":
            if player.coin_purse >= 100:
                player.coin_purse -= 100
                type_print(f"You head back home and pay off your debt with {player.coin_purse} gold to spare.\n")
                type_print("Congratulations. You won the game.\n")
                type_print("Created by Stephen Doty\n")
                break
            else:
                type_print("You don't have the 100 gold required to pay off your debt. Better head back into town and find some work.\n")
        elif raw_input == "7":
            type_print("Thanks for playing.\n")
            break
        else:
            type_print(f"Invalid input {raw_input}")

def character_creation():
    print("________________________________________________________________________________________________\n")
    type_print("Welcome to \"Hunter RPG\" where you play as a bounty hunter and fight monsters to earn money. Your goal is to \nearn at least 100 gold to pay off some accrued debt.\n\nIt's time to create your character.\n")
    type_print("Press \"Enter\" to continue")
    input()
    while True: 
        type_print("You can choose between three different classes - Barbarian, Medic, and Rogue.\n")
        type_print("1. The Barbarian has the most health (13 HP) and the most armor (10 AC) and will occasionally do double damage.")
        type_print("2. The Medic has less health (11 HP) but decent armor (9 AC) and will occasionally heal a bit in battle.")
        type_print("3. The Rogue has decent health (12 HP) and the lowest armor (8 AC) but will occasionally take half damage from attacks.\n")
        type_print("Which class could you like to play as?")
        print("> ", end = ' ')
        class_names = ["Barbarian", "Medic", "Rogue"]
        classes = [Barbarian, Medic, Rogue]
        raw_input = input()
        print("________________________________________________________________________________________________\n")
        if raw_input == "1" or raw_input == "2" or raw_input == "3":
            type_print(f"You have chosen {class_names[int(raw_input) - 1]}. Would you like to continue and name your character?\n")
            type_print("1. Yes")
            type_print("2. No")
            print("> ", end = ' ')
            raw_input2 = input()
            print("________________________________________________________________________________________________\n")
            if raw_input2 == "1":
                type_print("What would you like to name your character?\n")
                raw_input3 = input()
                print("________________________________________________________________________________________________\n")
                type_print(f"You will play as {raw_input3}, the {class_names[int(raw_input) - 1]}. Are you happy with this character?\n")
                type_print("1. Yes")
                type_print("2. No")
                print("> ", end = ' ')
                raw_input4 = input()
                print("________________________________________________________________________________________________\n")
                if raw_input4 == "1":
                    break
                elif raw_input4 == "2":
                    pass
                else:
                    type_print(f"Invalid input {raw_input}\n")
            elif raw_input2 == "2":
                pass
            else:
                type_print(f"Invalid input {raw_input}\n")
        else:
            type_print(f"Invalid input {raw_input}\n")
    class_type = classes[int(raw_input) - 1]
    player_name = raw_input3
    return class_type, player_name

# uncomment for character creation
class_type, player_name = character_creation()
player = class_type(race = "human", name = player_name)

# comment out to enable character creation
# player = Barbarian(race = "human")

player.coin_purse = 5

player.inventory = []

main(player)



# todo include import pickle to be able to save???

# todo add music and sound effects???

# todo add ASCII and other art/pictures
