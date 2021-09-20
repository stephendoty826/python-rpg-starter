from random import *

from rpg_classes import *

import rpg_functions

# town_list = ["Forstford", "MillerVille", "Dawsbury"]

def town(player):
    print("You arrive at the town of Dawsbury.\n")
    while True:
        print("What would you like to do?")
        print("1. Talk to the locals")
        print("2. View the bounty board")
        print("3. View current bounty")
        print("4. View inventory")
        print("5. View status")
        print("6. Shop for items")
        print("7. Rest at the inn (5 gold)")
        print("8. Leave town")
        print("> ", end = ' ')
        raw_input = input()
        print("________________________________________________________________________________________________\n")
        if raw_input == "1":
            talk_to_locals(player)
        elif raw_input == "2":
            if player.current_bounty != []:
                print(f"You current bounty is {player.current_bounty[0].name} ({player.current_bounty[0].race}) - {player.current_bounty[0].bounty} gold.\nWould you like to choose a different bounty?\n")
                print("1. Yes")
                print("2. No")
                print("> ", end = ' ')
                raw_input2 = input()
                print("________________________________________________________________________________________________\n")
                if raw_input2 == "1":
                    if player.current_bounty[0].is_specialty_bounty:
                        specialty_bounties.append(player.current_bounty[0])
                        player.current_bounty = []
                        bounty_board(player)
                    else:
                        player.current_bounty = []
                        bounty_board(player)
                elif raw_input2 == "2":
                    pass
                else:
                    print(f"Invalid input {raw_input}\n")
            else:
                bounty_board(player)
        elif raw_input == "3":
            rpg_functions.check_bounty(player)
        elif raw_input == "4":
            rpg_functions.check_inventory(player)
        elif raw_input == "5":
            player.print_status()
        elif raw_input == "6":
            shop(player)
        elif raw_input == "7":
            if player.coin_purse < 5:
                print("You don't have enough gold to stay at the inn. Turn in some bounties to earn some money.\n")
            else:
                player.health = player.max_hp
                player.coin_purse -= 5
                print(f"Your health is fully restored to {player.health} HP. You now have {player.coin_purse} gold.\n")
        elif raw_input == "8":
            break
        else:
            print(f"Invalid input {raw_input}\n")



def talk_to_locals(player):
    while True:
        print("Who do you want to talk to?\n")
        print("1. Old Man Brigham")
        print("2. Elder Liana")
        print("3. Small boy")
        print("4. Back")
        print("> ", end = ' ')
        raw_input = input()
        print("________________________________________________________________________________________________\n")
        if raw_input == "1":
            old_man_brigham()
        elif raw_input == "2":
            elder_liana()
        elif raw_input == "3":
            small_boy(player)
        elif raw_input == "4":
            break
        else:
            print(f"Invalid input {raw_input}\n")



standard_bounties = [goblin, shadow, troll]
specialty_bounties = [mudmug, stigg, undead_ned, big_nellie, lighthouse_shadow, fire_serpent]

def bounty_board(player):
    while True:
        print("Which bounties would you like to view?\n")
        print("1. Standard Bounties")
        print("2. Specialty Bounties")
        print("3. Back")
        print("> ", end = ' ')
        raw_input = input()
        print("________________________________________________________________________________________________\n")
        if raw_input == "1":
            print("The following standard bounties are avaiable. Please select which one you would like to take.\n")
            print("1. Goblin - 3 gold")
            print("2. Shadow - 6 gold")
            print("3. Troll - 10 gold")
            print("> ", end = ' ')
            raw_input2 = input()
            print("________________________________________________________________________________________________\n")
            try:
                if isinstance(int(raw_input2), int):
                    print(f"You have selected {standard_bounties[int(raw_input2) - 1].name}. Take this bounty?\n")
                    print("1. Yes")
                    print("2. No")
                    print("> ", end = ' ')
                    raw_input5 = input()
                    print("________________________________________________________________________________________________\n")
                    if raw_input5 == "1":
                        print(f"You have chosen {standard_bounties[int(raw_input2) - 1].name} as your bounty. Happy hunting!\n")
                        player.current_bounty.append(standard_bounties[int(raw_input2) - 1])
                        break
                    elif raw_input5 == "2":
                        pass
                    else:
                        print(f"Invalid input {raw_input5}\n")
            except:
                print(f"Invalid input {raw_input2}\n") 
        elif raw_input == "2":
            if specialty_bounties != []:
                print("The following specialty bounties are avaiable. Please select which one you would like to take.\n")
                count = 1
                for bounty in specialty_bounties:
                    print(f"{count}. {bounty.name} ({bounty.race}) - {bounty.bounty} gold")
                    count += 1
                print("> ", end = ' ')
                raw_input3 = input()
                print("________________________________________________________________________________________________\n")
                try:
                    if isinstance(int(raw_input3), int):
                        print("________________________________________________________________________________________________\n")
                        print(f"You have selected {specialty_bounties[int(raw_input3) - 1].name}. Take this bounty?\n")
                        print("1. Yes")
                        print("2. No")
                        print("> ", end = ' ')
                        raw_input4 = input()
                        print("________________________________________________________________________________________________\n")
                        if raw_input4 == "1":
                            print(f"You have chosen {specialty_bounties[int(raw_input3) - 1].name} as your bounty. Happy hunting!\n")
                            player.current_bounty.append(specialty_bounties[int(raw_input3) - 1])
                            del specialty_bounties[int(raw_input3) - 1]
                            break
                        elif raw_input4 == "2":
                            pass
                        else:
                            print(f"Invalid input {raw_input4}\n")
                except:
                    print(f"Invalid input {raw_input3}\n")
            else:
                print("All specialty bounties have been completed. Please feel free to check out our standard bounties.\n")
        elif raw_input == "3":
            break
        else:
            print(f"Invalid input {raw_input}\n")
    
standard_items = [super_tonic, firebomb, evade, water_balloon]
specialty_items = [ac_upgrade, hp_upgrade, to_hit_upgrade, greataxe, bug_in_bottle]

def shop(player):
    while True:
        print("Which items would you like to view?\n")
        print("1. Standard Items")
        print("2. Specialty Items")
        print("3. Back")
        print("> ", end = ' ')
        raw_input = input()
        print("________________________________________________________________________________________________\n")
        if raw_input == "1":
            print("The following standard items are available. Please select which one you would like to purchase.\n")
            count = 1
            for item in standard_items:
                print(f"{count}. {item.name}: ({item.description}) - {item.price} gold")
                count += 1
            print("> ", end = ' ')
            raw_input2 = input()
            print("________________________________________________________________________________________________\n") 
            try:
                if isinstance(int(raw_input2), int):
                    if player.coin_purse - standard_items[int(raw_input2) - 1].price < 0:
                        print("You don't have enough gold for that.")
                        pass
                    else:
                        print(f"You have selected {standard_items[int(raw_input2) - 1].name}. Purchase this item?\n")
                        print("1. Yes")
                        print("2. No")
                        print("> ", end = ' ')
                        raw_input5 = input()
                        print("________________________________________________________________________________________________\n")
                        if raw_input5 == "1":
                            print(f"You have purchased {standard_items[int(raw_input2) - 1].name}. You now have {player.coin_purse} gold.\n")
                            print(f"You now have {player.coin_purse} gold.\n")
                            player.inventory.append(standard_items[int(raw_input2) - 1])
                            player.coin_purse -= standard_items[int(raw_input2) - 1].price
                            break
                        elif raw_input5 == "2":
                            pass
                        else:
                            print(f"Invalid input {raw_input5}\n")
            except:
                print(f"Invalid input {raw_input2}\n") 
        elif raw_input == "2":
            if specialty_items != []:
                print("The following specialty items are avaiable. Please select which one you would like to purchase.\n")
                count = 1
                for item in specialty_items:
                    print(f"{count}. {item.name}: ({item.description}) - {item.price} gold")
                    count += 1
                print("> ", end = ' ')
                raw_input3 = input()
                print("________________________________________________________________________________________________\n")
                try:
                    if isinstance(int(raw_input3), int):
                        if player.coin_purse - specialty_items[int(raw_input3) - 1].price < 0:
                            print("You don't have enough gold for that.")
                            pass
                        else:
                            print(f"You have selected {specialty_items[int(raw_input3) - 1].name}. Purchase this item?\n")
                            print("1. Yes")
                            print("2. No")
                            print("> ", end = ' ')
                            raw_input4 = input()
                            print("________________________________________________________________________________________________\n")
                            if raw_input4 == "1":
                                specialty_items[int(raw_input3) - 1].use(player)
                                player.coin_purse -= specialty_items[int(raw_input3) - 1].price
                                del specialty_items[int(raw_input3) - 1]
                                break
                            elif raw_input4 == "2":
                                pass
                            else:
                                print(f"Invalid input {raw_input4}\n")
                except:
                    print(f"Invalid input {raw_input3}\n")
            else:
                print("We are sold out of specialty items. Please feel free to check out our standard items.\n")
        elif raw_input == "3":
            break
        else:
            print(f"Invalid input {raw_input}\n")



def old_man_brigham():
    print("Well, hello there. You must be one of those adventuring types.\n")
    index = 0
    while True:
        print("1. Talk to Old Man Brigham")
        print("2. Back")
        print("> ", end = ' ')
        raw_input = input()
        print("________________________________________________________________________________________________\n")
        response_list = ["Ned who lives in the farmhouse always said he wanted to be cremated. Well, now that he's dead maybe he'll get his wish.", "GO ON! GIT OUTTA HERE! Sorry...these darn kids keep running through my yard.", "Have you spoken to our village elder? Liana's such a nice lady. I remember when she was just a little girl following after her mother...", "People say I've got a few screws loose but I'll tell you what, if you got a fire you want put out, throw some water on it. \nThat's all I'm sayin'...that's all.", "Back in my day, we used to work for a living. Not like Lynette and her two boys, always running around whilly nilly and such."]
        if raw_input == "1":
            if index == len(response_list):
                index = 0
                print(f"{response_list[index]}\n")
                index += 1
            else:
                print(f"{response_list[index]}\n")
                index += 1
        elif raw_input == "2":
            break
        else:
            print(f"Invalid input {raw_input}\n")



def elder_liana():
    print("Hello, I am the village elder. My name is Liana.\n")
    index = 0
    while True:
        print("1. Talk to Elder Liana")
        print("2. Back")
        print("> ", end = ' ')
        raw_input = input()
        print("________________________________________________________________________________________________\n")
        response_list = ["If it's not to much to ask, our town has need of your help. We normally get supplied from the town north of \nhere, but a fire serpent has recently made that area her hunting ground and now we can't get proper supplies.", "Old man Ned died recently and well...he's not as dead as he once was. Now his corpse roams the old farm house and attacks anyone who goes near.", "Ever heard of Big Nellie. That troll has caused us a lot of trouble in recent months. So much so that her head's worth double the normal bounty.", "Feel free to look at our bounty board if your interested in some work. It has standard bounties you can do multiple times \nand specialty bounties you can only do once. The specialty bounties pay better but the target is harder."]
        if raw_input == "1":
            if index == len(response_list):
                index = 0
                print(f"{response_list[index]}\n")
                index += 1
            else:
                print(f"{response_list[index]}\n")
                index += 1
        elif raw_input == "2":
            break
        else:
            print(f"Invalid input {raw_input}\n")



def small_boy(player):
    print("Sell me something. Please sell me something with \"C\".\n")
    while True:
        print("1. Show the small boy what's in your pack.")
        print("2. Back")
        print("> ", end = ' ')
        raw_input = input()
        print("________________________________________________________________________________________________\n")
        if raw_input == "1":
            if player.has_bug:
                print("Oh, how cute. I'll buy that bug for 15 gold.\n")
                print("1. Sell the bug.")
                print("2. Keep the bug.")
                raw_input2 = input()
                print("________________________________________________________________________________________________\n")
                if raw_input2 == "1":
                    print("Yay! I get my own little friend. I will name him Albert and he will be my friend.\n")
                    player.coin_purse += 15
                    player.has_bug = False
                    print(f"You sold the bug for 15 gold. Now you have {player.coin_purse} gold.\n")
                elif raw_input2 == "2":
                    print("Oh, you're no fun. Well, if you change your mind, you know where to find me.\n")
                else:
                    print(f"Invalid input {raw_input}\n")
            else:
                print("I don't want any of that stuff. Don't you have anything interesting?\n")
        elif raw_input == "2":
            break
        else:
            print(f"Invalid input {raw_input}\n")
        
#todo continue setting up town




