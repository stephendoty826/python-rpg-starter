from random import *

import rpg_classes

Fighter = rpg_classes.Fighter
Medic = rpg_classes.Medic
Rogue = rpg_classes.Rogue

Goblin = rpg_classes.Goblin
Zombie = rpg_classes.Zombie
Shadow = rpg_classes.Shadow
Fire_Serpent = rpg_classes.Fire_Serpent
Helper = rpg_classes.Helper
Store = rpg_classes.Store

#todo implement multiple heros/enemies? 

def battle(player, enemy):
    combat_turn = 1

    print(f"\nYou come across a {enemy.race}.\n")
    while enemy.alive() and player.alive():
        player.print_status()
        enemy.print_status()
        print("\nWhat do you want to do?")
        print(f"1. Fight {enemy.race}")
        print("2. Spy")
        print("3. Use an item")
        print("4. Do nothing")
        print("5. Flee")
        print("> ", end = ' ')
        raw_input = input()
        print("________________________________________________________________________________________________\n")
        if raw_input == "1":
            # Player attacks enemy
            player.attack(enemy)
            if enemy.health <= 0:
                print(f"The {enemy.race} is dead.\n")
                player.coin_purse += enemy.bounty
                print(f"{player.name} received {enemy.bounty} coins for a total of {player.coin_purse}.")
                print("________________________________________________________________________________________________\n")
                if Helper.is_zombie(enemy): # enemy is a zombie and it can't be killed. 
                    enemy.undead()
                    print("Moments later, the zombie slowly rises to it's feet again. This thing just won't die.\n")
                    print("________________________________________________________________________________________________\n")
        elif raw_input == "2":
            player.spy(enemy)
        elif raw_input == "3":
            # Store.use_firebomb(player, enemy)
            Store.use_tonic(player)
            if enemy.health <= 0:
                if Helper.is_zombie(enemy):
                    print(f"The {enemy.race} is truly dead this time.\n")
                    player.coin_purse += enemy.bounty
                    print(f"{player.name} received {enemy.bounty} coins for a total of {player.coin_purse}.")
                else:
                    print(f"The {enemy.race} is dead.\n")
                    player.coin_purse += enemy.bounty
                    print(f"{player.name} received {enemy.bounty} coins for a total of {player.coin_purse}.")
                print("________________________________________________________________________________________________\n")
        elif raw_input == "4":
            pass
        elif raw_input == "5":
            print("Goodbye.\n")
            break
        else:
            print(f"Invalid input {raw_input}\n")
        if enemy.health > 0:
            # Enemy attacks player
            if Helper.is_fighter(player):
                enemy.attack(player)
                print("________________________________________________________________________________________________\n")
            if Helper.is_medic(player):
                enemy.attack(player)
                player.heal()
                print("________________________________________________________________________________________________\n")
            if Helper.is_rogue(player):
                if player.chance_evade():
                    enemy.rogue_evade_attack(player)
                    print("________________________________________________________________________________________________\n")
                else:
                    enemy.attack(player)
                    print("________________________________________________________________________________________________\n")
            if player.health <= 0:
                print(f"{player.name} is dead.")
                print("________________________________________________________________________________________________\n")
        combat_turn += 1
