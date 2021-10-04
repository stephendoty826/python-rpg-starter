from random import *

import rpg_functions

import rpg_classes

Fighter = rpg_classes.Fighter
Medic = rpg_classes.Medic
Rogue = rpg_classes.Rogue

Goblin = rpg_classes.Goblin
Zombie = rpg_classes.Zombie
Shadow = rpg_classes.Shadow
Troll = rpg_classes.Troll
Fire_Serpent = rpg_classes.Fire_Serpent
Helper = rpg_classes.Helper

Firebomb = rpg_classes.Firebomb
Super_Tonic = rpg_classes.Super_Tonic
Evade = rpg_classes.Evade

evade = Evade()

#todo implement multiple heros/enemies? 

def battle(player, enemy):
    combat_turn = 1
    is_evading = -1
    print(f"\nYou spot your bounty in the distance, a lone {enemy.race}.\n")
    while enemy.alive() and player.alive():
        player.print_status()
        print("What do you want to do?")
        print(f"1. Attack {enemy.race}")
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
                if Helper.is_zombie(enemy): # enemy is a zombie and it can't be killed. 
                    enemy.undead()
                    print("Moments later, the zombie slowly rises to it's feet again. This thing just won't die.\n")
                    print("________________________________________________________________________________________________\n")
                else:
                    player.current_bounty = []
                    player.coin_purse += enemy.bounty
                    print(f"{player.name} received {enemy.bounty} gold. You now have {player.coin_purse} gold.")
                    print("________________________________________________________________________________________________\n")
        elif raw_input == "2":
            player.spy(enemy)
        elif raw_input == "3":
            rpg_functions.use_item(player, enemy)
            if player.is_evading:
                player.armor += 4
                is_evading = 2
            if enemy.health <= 0:
                if Helper.is_zombie(enemy):
                    print(f"The {enemy.race} is truly dead this time.\n")
                    player.current_bounty = []
                    player.coin_purse += enemy.bounty
                    print(f"{player.name} received {enemy.bounty} gold. You now have {player.coin_purse} gold.")
                else:
                    print(f"The {enemy.race} is dead.\n")
                    player.current_bounty = []
                    player.coin_purse += enemy.bounty
                    print(f"{player.name} received {enemy.bounty} gold. You now have {player.coin_purse} gold.")
                print("________________________________________________________________________________________________\n")
        elif raw_input == "4":
            pass
        elif raw_input == "5":
            print("You flee and from the fight.\n")
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
            if is_evading > 0:
                is_evading -= 1
            elif is_evading == 0:
                player.armor -= 4
                player.is_evading = False
                is_evading = -1
            if player.health <= 0:
                print(f"{player.name} is dead.")
                print("________________________________________________________________________________________________\n")
        combat_turn += 1
    #todo have line where player regens small amount of health after battle
