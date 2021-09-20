from random import *

import rpg_classes

evade = rpg_classes.Evade()

#todo function for randomizing enemy

def check_bounty(player):
    if player.current_bounty == []:
        print("You currently don't have a bounty. Be sure to check the bounty board in town to grab one.\n ")
    else:
        print(f"You current bounty is {player.current_bounty[0].name} ({player.current_bounty[0].race}) - {player.current_bounty[0].bounty} gold.\n")

def check_inventory(player):
    if player.inventory == []:
        print("You currently don't have any items. Be sure to check visit the shop the buy some.")
        print(f"{player.coin_purse} gold.\n")
    else:
        print(f"You are carrying the following items.\n")
        for i in range(len(player.inventory)):
            print(f"{player.inventory[i].name}: - {player.inventory[i].description}")
        print(f"{player.coin_purse} gold.\n")

def use_item(player, enemy):
    if player.inventory == []:
        print("You currently don't have any items. Be sure to check visit the shop the buy some.")
        print(f"{player.coin_purse} gold.\n")
    else:
        print(f"You are carrying the following items. Which item would you like to use?\n")
        count = 1
        for item in player.inventory:
            print(f"{count}. {item.name}: - {item.description}")
            count += 1
        print("> ", end = ' ')
        raw_input = input()
        print("________________________________________________________________________________________________\n")
        try:
            if isinstance(int(raw_input), int):
                player.inventory[int(raw_input) - 1].use(player, enemy)
                del player.inventory[int(raw_input) - 1]
        except:
            print(f"Invalid input {raw_input}\n") 


#todo function for character creation

#todo combat options differ depending on the type of player character

#todo have player races differ in some way (super special ability or other?)





