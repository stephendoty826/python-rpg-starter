from random import *

from rpg_functions import *

import rpg_classes

Barbarian = rpg_classes.Barbarian
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
# Evade = rpg_classes.Evade

# evade = Evade()

#todo implement multiple heros/enemies? 

def battle(player, enemy):
    combat_turn = 1
    is_evading = -1
    type_print(f"\nYou spot your bounty in the distance, a lone {enemy.race}.\n")
    while enemy.alive() and player.alive():
        player.print_status()
        type_print("What do you want to do?")
        type_print(f"1. Attack {enemy.race}")
        type_print("2. Spy")
        type_print("3. Use an item")
        type_print("4. Do nothing")
        type_print("5. Flee")
        print("> ", end = ' ')
        raw_input = input()
        print("________________________________________________________________________________________________\n")
        if raw_input == "1":
            # Player attacks enemy
            player.attack(enemy)
            #todo player.fire_serpent_burns is running and hurting the player even when he misses the fire serpent.
            player.fire_serpent_burns(enemy)
            if enemy.health <= 0:
                type_print(f"The {enemy.race} is dead.\n")
                if Helper.is_zombie(enemy): # enemy is a zombie and it can't be killed. 
                    enemy.undead()
                    type_print("Moments later, the zombie slowly rises to it's feet again. This thing just won't die.\n")
                    print("________________________________________________________________________________________________\n")
                else:
                    player.current_bounty = []
                    player.coin_purse += enemy.bounty
                    type_print(f"{player.name} received {enemy.bounty} gold. You now have {player.coin_purse} gold.")
                    print("________________________________________________________________________________________________\n")
        elif raw_input == "2":
            player.spy(enemy)
        elif raw_input == "3":
            use_item(player, enemy)
            if player.is_evading:
                player.armor += 4
                is_evading = 2
            if enemy.health <= 0:
                if Helper.is_zombie(enemy):
                    type_print(f"The {enemy.race} is truly dead this time.\n")
                    player.current_bounty = []
                    player.coin_purse += enemy.bounty
                    type_print(f"{player.name} received {enemy.bounty} gold. You now have {player.coin_purse} gold.")
                else:
                    type_print(f"The {enemy.race} is dead.\n")
                    player.current_bounty = []
                    player.coin_purse += enemy.bounty
                    type_print(f"{player.name} received {enemy.bounty} gold. You now have {player.coin_purse} gold.")
                print("________________________________________________________________________________________________\n")
        elif raw_input == "4":
            pass
        elif raw_input == "5":
            type_print("You flee and from the fight.\n")
            break
        else:
            type_print(f"Invalid input {raw_input}\n")
        if enemy.health > 0:
            # Enemy attacks player
            if Helper.is_barbarian(player):
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
                type_print(f"{player.name} is dead.")
                print("________________________________________________________________________________________________\n")
        combat_turn += 1
    #todo game crashes when player dies...this still tries to run and heal the player
    # player attempts to bandage their wounds after battle to regain a small amount of health. 
    if player.health < player.max_hp:
        first_aid = randint(1, 3)
        player.health += health_regen
        if first_aid == 3:
            health_regen = randint(1, 2)
            if player.health >= player.max_hp:
                player.health = player.max_hp
                type_print(f"After the battle, you bandaged your wounds and are back up to full health.\n")
            else:
                type_print(f"After the battle, you bandage your wounds and regain {health_regen} health.\n")
        else:
            type_print(f"After the battle, you attempt to bandage your wounds but fail to do any healing.\n")

    

