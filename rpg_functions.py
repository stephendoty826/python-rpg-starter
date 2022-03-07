from random import *

# import rpg_classes

import time

# evade = rpg_classes.Evade()



def check_bounty(player):
    if player.current_bounty == []:
        type_print("You currently don't have a bounty. Be sure to check the bounty board in town to grab one.\n ")
    else:
        type_print(f"You current bounty is {player.current_bounty[0].name} ({player.current_bounty[0].race}) - {player.current_bounty[0].bounty} gold.\n")

def check_inventory(player):
    if player.inventory == []:
        type_print("You currently don't have any items. Be sure to visit the shop the buy some.")
        type_print(f"You have {player.coin_purse} gold.\n")
    else:
        type_print(f"You are carrying the following items.\n")
        for i in range(len(player.inventory)):
            type_print(f"{player.inventory[i].name}: - {player.inventory[i].description}")
        type_print(f"You have {player.coin_purse} gold.\n")

def use_item(player, enemy):
    if player.inventory == []:
        type_print("You currently don't have any items. Be sure to visit the shop the buy some.")
        type_print(f"You have {player.coin_purse} gold.\n")
    else:
        type_print(f"You are carrying the following items. Which item would you like to use?\n")
        count = 1
        for item in player.inventory:
            type_print(f"{count}. {item.name}: - {item.description}")
            count += 1
        print("> ", end = ' ')
        raw_input = input()
        print("________________________________________________________________________________________________\n")
        try:
            if isinstance(int(raw_input), int):
                player.inventory[int(raw_input) - 1].use(player, enemy)
                del player.inventory[int(raw_input) - 1]
        except:
            type_print(f"Invalid input {raw_input}\n") 

# Text Printing Functions
def type_print(string):
    for i in string:
        print(i, end = '', flush = True)
        time.sleep(0.005)
    print()

def slow_type_print(string):
    for i in string:
        print(i, end = '', flush = True)
        time.sleep(0.0325)
    print()

def first_aid(player):
    if player.health < player.max_hp:
        healing = randint(1, 3)
        if healing == 3:
            health_regen = randint(1, 2)
            player.health += health_regen
            if player.health >= player.max_hp:
                player.health = player.max_hp
                type_print(f"After the battle, you bandaged your wounds and are back up to full health.\n")
            else:
                type_print(f"After the battle, you bandage your wounds and regain {health_regen} health.\n")
        else:
            type_print(f"After the battle, you attempt to bandage your wounds but fail to do any healing.\n")

#todo combat options differ depending on the type of player character

#todo have player races differ in some way (super special ability or other?)






