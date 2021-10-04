import time

from rpg_battle import *

from rpg_town import *

fighter = Fighter(race = "human")
medic = Medic(race = "human")
rogue = Rogue(race = "human")

# store = [Helper.SuperTonic]

# store_description = {
#     "Super Tonic": "A tonic that restores 10 HP. Can be used in battle."
#     }

def main(player):
    # time.sleep(1)
    print(f"With only {player.coin_purse} gold to your name, you start searching for bounties. Better head into town and grab one.\n")
    town(player)
    while True:
        print("What do you want to do?")
        print(f"1. Fight your bounty")
        print("2. Go to town")
        print("3. View current bounty")
        print("4. View inventory")
        print("5. View status")
        print("6. Pay off debt.")
        print("7. Quit")
        # print("3. Explore.")
        print("> ", end = ' ')
        raw_input = input()
        print("________________________________________________________________________________________________\n")
        if raw_input == "1":
            # choose enemy function
            if player.current_bounty == []:
                print("You currently don't have a bounty. Be sure to check the bounty board in town to grab one.\n ")
            else:
                battle(player, player.current_bounty[0])
        elif raw_input == "2":
            town(player)
        elif raw_input == "3":
            if player.current_bounty == []:
                print("You currently don't have a bounty. Be sure to check the bounty board in town to grab one.\n ")
            else:
                print(f"You current bounty is {player.current_bounty[0].name} ({player.current_bounty[0].race}) - {player.current_bounty[0].bounty} gold.\n")
        elif raw_input == "4":
            rpg_functions.check_inventory(player)
        elif raw_input == "5":
            player.print_status()
        elif raw_input == "6":
            if player.coin_purse >= 100:
                print("You head back home and pay off your debt.\n")
                print("Congratulations. You won the game.\n")
                print("Created by Stephen Doty\n")
                break
            else:
                print("You don't have the 100 gold required to pay off your debt. Better head back into town and find some work.\n6")
        elif raw_input == "7":
            print("Thanks for playing.\n")
            break
        else:
            print(f"Invalid input {raw_input}")

def character_creation():
    print("\nWelcome to \"Hunter RPG\" where you play as a bounty hunter and fight monsters to earn money. Your goal is to \nearn at least 100 gold to pay off some accrued debt.\n")
    print("It's time to create your character.")
    print("You can choose between three different classes - Figher, Medic and Rogue.\n")
    while True: 
        print("1. The Fighter has the most health (13 HP) and the most armor (10 AC) and will occasionally do double damage.")
        print("2. The Medic has less health (11 HP) but decent armor (9 AC) and will occasionally heal a bit in battle.")
        print("3. The Rogue has decent health (12 HP) and the lowest armor (8 AC) but will occasionally take half damage from attacks.\n")
        print("Which class could you like to play as?")
        print("> ", end = ' ')
        class_names = ["Fighter", "Medic", "Rogue"]
        classes = [Fighter, Medic, Rogue]
        raw_input = input()
        print("________________________________________________________________________________________________\n")
        if raw_input == "1" or raw_input == "2" or raw_input == "3":
            print(f"You have chosen {class_names[int(raw_input) - 1]}. Would you like to continue and name your character?\n")
            print("1. Yes")
            print("2. No")
            print("> ", end = ' ')
            raw_input2 = input()
            print("________________________________________________________________________________________________\n")
            if raw_input2 == "1":
                print("What would you like to name your character?\n")
                raw_input3 = input()
                print("________________________________________________________________________________________________\n")
                print(f"You will play as {raw_input3}, the {class_names[int(raw_input) - 1]}. Are you happy with this character?\n")
                print("1. Yes")
                print("2. No")
                print("> ", end = ' ')
                raw_input4 = input()
                print("________________________________________________________________________________________________\n")
                if raw_input4 == "1":
                    break
                elif raw_input4 == "2":
                    pass
                else:
                    print(f"Invalid input {raw_input}\n")
            elif raw_input2 == "2":
                pass
            else:
                print(f"Invalid input {raw_input}\n")
        else:
            print(f"Invalid input {raw_input}\n")
    class_type = classes[int(raw_input) - 1]
    player_name = raw_input3
    return class_type, player_name

class_type, player_name = character_creation()
player = class_type(race = "human", name = player_name)

player.coin_purse = 5

main(player)

# todo import time and use time.sleep(<your time here>) to have text scroll 
    # There are different ways to do it, depending on how you want it to print out.

# todo include import pickle to be able to save???

# todo add music and sound effects???

# todo add ASCII and other art/pictures
