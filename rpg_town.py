from random import *

from rpg_classes import *

from rpg_functions import *

# town_list = ["Forstford", "MillerVille", "Dawsbury"]

def town(player):
    type_print("You arrive at the town of Dawsbury.")
    while True:
        type_print("\nWhat would you like to do?\n")
        type_print("1. Talk to the locals")
        type_print("2. View the bounty board")
        type_print("3. View current bounty")
        type_print("4. View inventory")
        type_print("5. View status")
        type_print("6. Shop for items")
        type_print("7. Rest at the inn (5 gold)")
        type_print("8. Leave town")
        print("> ", end = ' ')
        raw_input = input()
        print("________________________________________________________________________________________________\n")
        if raw_input == "1":
            talk_to_locals(player)
        elif raw_input == "2":
            if player.current_bounty != []:
                type_print(f"You current bounty is {player.current_bounty[0].name} ({player.current_bounty[0].race}) - {player.current_bounty[0].bounty} gold.\nWould you like to choose a different bounty?\n")
                type_print("1. Yes")
                type_print("2. No")
                print("> ", end = ' ')
                raw_input2 = input()
                print("________________________________________________________________________________________________\n")
                if raw_input2 == "1":
                    if player.current_bounty[0].is_specialty_bounty:
                        bounties.specialty_bounties.append(player.current_bounty[0])
                        player.current_bounty = []
                        bounty_board(player)
                    else:
                        player.current_bounty = []
                        bounty_board(player)
                elif raw_input2 == "2":
                    pass
                else:
                    type_print(f"Invalid input {raw_input}\n")
            else:
                bounty_board(player)
        elif raw_input == "3":
            check_bounty(player)
        elif raw_input == "4":
            check_inventory(player)
        elif raw_input == "5":
            player.print_status()
        elif raw_input == "6":
            shop(player)
        elif raw_input == "7":
            type_print("Resting at the inn will fully restore your health. Rest for 5 gold?\n")
            type_print("1. Yes")
            type_print("2. No")
            type_print(f"You have {player.coin_purse} gold.")
            print("> ", end = ' ')
            rest_input = input()
            if rest_input == "1":
                if player.coin_purse < 5:
                    type_print("\nYou don't have enough gold to stay at the inn. Turn in some bounties to earn some money.")
                else:
                    player.health = player.max_hp
                    player.coin_purse -= 5
                    type_print(f"\nYour health is fully restored to {player.health} HP. You now have {player.coin_purse} gold.")
            else:
                pass
        elif raw_input == "8":
            break
        else:
            type_print(f"Invalid input {raw_input}\n")



def talk_to_locals(player):
    while True:
        type_print("\nWho do you want to talk to?\n")
        type_print("1. Old Man Brigham")
        type_print("2. Elder Liana")
        type_print("3. Small boy")
        type_print("4. Back")
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
            type_print(f"Invalid input {raw_input}\n")

def bounty_board(player):
    # function to reset bounty board
    goblin = Goblin()
    shadow = Shadow()
    troll = Troll()
    bounties.standard_bounties = [goblin, shadow, troll]
    while True:
        type_print("\nWhich bounties would you like to view?\n")
        type_print("1. Standard Bounties")
        type_print("2. Specialty Bounties")
        type_print("3. Back")
        print("> ", end = ' ')
        raw_input = input()
        print("________________________________________________________________________________________________\n")
        if raw_input == "1":
            type_print("The following standard bounties are avaiable. Please select which one you would like to take.\n")
            type_print(f"1. Goblin - {goblin.bounty} gold")
            type_print(f"2. Shadow - {shadow.bounty} gold")
            type_print(f"3. Troll - {troll.bounty} gold")
            type_print("4. Back")
            type_print(f"You have {player.coin_purse} gold.")
            print("> ", end = ' ')
            raw_input2 = input()
            print("________________________________________________________________________________________________\n")
            try:
                if raw_input2 == "4":
                    pass
                else:
                    if isinstance(int(raw_input2), int):
                        type_print(f"You have selected {bounties.standard_bounties[int(raw_input2) - 1].name}. Take this bounty?\n")
                        type_print("1. Yes")
                        type_print("2. No")
                        print("> ", end = ' ')
                        raw_input5 = input()
                        print("________________________________________________________________________________________________\n")
                        if raw_input5 == "1":
                            type_print(f"You have chosen {bounties.standard_bounties[int(raw_input2) - 1].name} as your bounty. Happy hunting!\n")
                            player.current_bounty.append(bounties.standard_bounties[int(raw_input2) - 1])
                            break
                        elif raw_input5 == "2":
                            pass
                        else:
                            type_print(f"Invalid input {raw_input5}\n")
            except:
                type_print(f"Invalid input {raw_input2}\n") 
        elif raw_input == "2":
            if bounties.specialty_bounties != []:
                type_print("The following specialty bounties are avaiable. Please select which one you would like to take.\n")
                count = 1
                for bounty in bounties.specialty_bounties:
                    type_print(f"{count}. {bounty.name} ({bounty.race}) - {bounty.bounty} gold")
                    count += 1
                type_print(f"{count}. Back")
                type_print(f"You have {player.coin_purse} gold.")
                print("> ", end = ' ')
                raw_input3 = input()
                print("________________________________________________________________________________________________\n")
                try:
                    # count equals index of bounties.specialty_bounties + 1
                    if int(raw_input3) == count:
                        pass
                    else:
                        if isinstance(int(raw_input3), int):
                            type_print(f"You have selected {bounties.specialty_bounties[int(raw_input3) - 1].name}. Take this bounty?\n")
                            type_print("1. Yes")
                            type_print("2. No")
                            print("> ", end = ' ')
                            raw_input4 = input()
                            print("________________________________________________________________________________________________\n")
                            if raw_input4 == "1":
                                type_print(f"You have chosen {bounties.specialty_bounties[int(raw_input3) - 1].name} as your bounty. Happy hunting!\n")
                                player.current_bounty.append(bounties.specialty_bounties[int(raw_input3) - 1])
                                del bounties.specialty_bounties[int(raw_input3) - 1]
                                break
                            elif raw_input4 == "2":
                                pass
                            else:
                                type_print(f"Invalid input {raw_input4}\n")
                except:
                    type_print(f"Invalid input {raw_input3}\n")
            else:
                type_print("All specialty bounties have been completed. Please feel free to check out our standard bounties.\n")
        elif raw_input == "3":
            break
        else:
            type_print(f"Invalid input {raw_input}\n")
    
standard_items = [super_tonic, firebomb, evade, water_balloon]
specialty_items = [ac_upgrade, hp_upgrade, to_hit_upgrade, greataxe, bug_in_bottle]

def shop(player):
    while True:
        type_print("\nWhich items would you like to view?\n")
        type_print("1. Standard Items")
        type_print("2. Specialty Items")
        type_print("3. Back")
        print("> ", end = ' ')
        raw_input = input()
        print("________________________________________________________________________________________________\n")
        if raw_input == "1":
            type_print("The following standard items are available. Please select which one you would like to purchase.\n")
            count = 1
            for item in standard_items:
                type_print(f"{count}. {item.name}: ({item.description}) - {item.price} gold")
                count += 1
            type_print(f"You have {player.coin_purse} gold.")
            print("> ", end = ' ')
            raw_input2 = input()
            print("________________________________________________________________________________________________\n") 
            try:
                if isinstance(int(raw_input2), int):
                    if player.coin_purse - standard_items[int(raw_input2) - 1].price < 0:
                        type_print("You don't have enough gold for that.")
                        pass
                    else:
                        type_print(f"You have selected {standard_items[int(raw_input2) - 1].name}. Purchase this item for {standard_items[int(raw_input2) - 1].price} gold?\n")
                        type_print("1. Yes")
                        type_print("2. No")
                        type_print(f"You have {player.coin_purse} gold.")
                        print("> ", end = ' ')
                        raw_input5 = input()
                        print("________________________________________________________________________________________________\n")
                        if raw_input5 == "1":
                            player.coin_purse -= standard_items[int(raw_input2) - 1].price
                            type_print(f"You have purchased {standard_items[int(raw_input2) - 1].name}. You now have {player.coin_purse} gold.\n")
                            player.inventory.append(standard_items[int(raw_input2) - 1])
                            break
                        elif raw_input5 == "2":
                            pass
                        else:
                            type_print(f"Invalid input {raw_input5}\n")
            except:
                type_print(f"Invalid input {raw_input2}\n") 
        elif raw_input == "2":
            if specialty_items != []:
                type_print("The following specialty items are avaiable. Please select which one you would like to purchase.\n")
                count = 1
                for item in specialty_items:
                    type_print(f"{count}. {item.name}: ({item.description}) - {item.price} gold")
                    count += 1
                type_print(f"You have {player.coin_purse} gold.")
                print("> ", end = ' ')
                raw_input3 = input()
                print("________________________________________________________________________________________________\n")
                try:
                    if isinstance(int(raw_input3), int):
                        if player.coin_purse - specialty_items[int(raw_input3) - 1].price < 0:
                            type_print("You don't have enough gold for that.")
                            pass
                        else:
                            type_print(f"You have selected {specialty_items[int(raw_input3) - 1].name}. Purchase this item for {specialty_items[int(raw_input3) - 1].price} gold?\n")
                            type_print("1. Yes")
                            type_print("2. No")
                            type_print(f"You have {player.coin_purse} gold.")
                            print("> ", end = ' ')
                            raw_input4 = input()
                            print("________________________________________________________________________________________________\n")
                            if raw_input4 == "1":
                                player.coin_purse -= specialty_items[int(raw_input3) - 1].price
                                specialty_items[int(raw_input3) - 1].use(player)
                                del specialty_items[int(raw_input3) - 1]
                                break
                            elif raw_input4 == "2":
                                pass
                            else:
                                type_print(f"Invalid input {raw_input4}\n")
                except:
                    print("test")
                    type_print(f"Invalid input {raw_input3}\n")
            else:
                type_print("We are sold out of specialty items. Please feel free to check out our standard items.\n")
        elif raw_input == "3":
            break
        else:
            type_print(f"Invalid input {raw_input}\n")



def old_man_brigham():
    type_print("\nWell, hello there. You must be one of those adventuring types.\n")
    index = 0
    while True:
        type_print("1. Talk to Old Man Brigham")
        type_print("2. Back")
        print("> ", end = ' ')
        raw_input = input()
        print("________________________________________________________________________________________________\n")
        response_list = ["Ned who lives in the farmhouse always said he wanted to be cremated. Well, now that he's dead maybe he'll get his wish.", "GO ON...GIT! These darn kids...always runnin' through my yard.", "Have you spoken to our village elder? Liana's such a nice lady. I remember when she was just a little girl following after her mother...", "I'll tell you what, if you got a fire you want put out, just throw some water on it. \nThat's all I'm sayin'...that's all.", "Back in my day, we used to work for a living. Not like Lynette and her two boys, always running around whilly nilly and such."]
        if raw_input == "1":
            if index == len(response_list):
                index = 0
                type_print(f"{response_list[index]}\n")
                index += 1
            else:
                type_print(f"{response_list[index]}\n")
                index += 1
        elif raw_input == "2":
            break
        else:
            type_print(f"Invalid input {raw_input}\n")



def elder_liana():
    type_print("\nHello, I am the village elder. My name is Liana.\n")
    index = 0
    while True:
        type_print("1. Talk to Elder Liana")
        type_print("2. Back")
        print("> ", end = ' ')
        raw_input = input()
        print("________________________________________________________________________________________________\n")
        response_list = ["If it's not to much to ask, our town has need of your help. We normally get supplied from the town north of \nhere, but a fire serpent has recently made that area her hunting ground and now we can't get proper supplies.", "Old Farmer Ned died recently and well...he's not as dead as he once was. Now his corpse roams the old farm house and attacks anyone who goes near.", "Ever heard of Big Nellie. That troll has caused us a lot of trouble in recent months. So much so that her head's worth double the normal bounty.", "Feel free to look at our bounty board if your interested in some work. It has standard bounties you can do multiple times \nand specialty bounties you can only do once. The specialty bounties pay better but the target is harder."]
        if raw_input == "1":
            if index == len(response_list):
                index = 0
                type_print(f"{response_list[index]}\n")
                index += 1
            else:
                type_print(f"{response_list[index]}\n")
                index += 1
        elif raw_input == "2":
            break
        else:
            type_print(f"Invalid input {raw_input}\n")

def small_boy(player):
    type_print("\nSell me something. Please sell me something with \"C\". [says the boy as he eagerly bounces up and down.]\n")
    while True:
        type_print("1. Show the small boy what's in your pack.")
        type_print("2. Back")
        print("> ", end = ' ')
        raw_input = input()
        print("________________________________________________________________________________________________\n")
        if raw_input == "1":
            if player.has_bug:
                type_print("Oh, how cute. I'll buy that bug for 15 gold.\n")
                type_print("1. Sell the bug.")
                type_print("2. Keep the bug.")
                print("> ", end = ' ')
                raw_input2 = input()
                print("________________________________________________________________________________________________\n")
                if raw_input2 == "1":
                    type_print("Yay! I get my own little friend. I will name him Albert and he will be my friend.\n")
                    player.coin_purse += 15
                    player.has_bug = False
                    type_print(f"You sold the bug for 15 gold. Now you have {player.coin_purse} gold.\n")
                elif raw_input2 == "2":
                    type_print("Oh, you're no fun. Well, if you change your mind, you know where to find me.\n")
                else:
                    type_print(f"Invalid input {raw_input}\n")
            # use boy_inventory to store water baloons he has purchased
            elif player.playHasWaterBaloon() and boy.inventory_not_full():
                type_print("A water baloon...I WANT IT. Let me buy it from you.\n")
                type_print("1. Sell a water balloon.")
                type_print("2. Back.")
                print("> ", end = ' ')
                sell_balloon_input = input()
                if sell_balloon_input == "1":
                    type_print("Horray! Now I can have a water baloon fight with my friends.\n")
                    player.inventory
                    player.coin_purse += 3
                    boy.buy_water_balloon(player)
                    type_print(f"You sold a water balloon for 3 gold. Now you have {player.coin_purse} gold.\n")
                elif sell_balloon_input == "2":
                    type_print("Oh, you're no fun. Well, if you change your mind, you know where to find me.\n")
                else:
                    type_print(f"Invalid input {sell_balloon_input}\n")
            else:
                type_print("I don't want any of that stuff. Don't you have anything interesting?\n")
        elif raw_input == "2":
            break
        else:
            type_print(f"Invalid input {raw_input}\n")





