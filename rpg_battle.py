from random import *

# from rpg_classes import *

#todo implement multiple heros/enemies?

def battle(player, enemy):
    combat_turn = 1
    count = 1
    while enemy.alive() and player.alive():
        print()
        player.print_status()
        enemy.print_status()
        print()
        print(f"There is a single {enemy.race}.")
        print()
        print("What do you want to do?")
        print(f"1. Fight {enemy.race}")
        print("2. Spy")
        print("3. Do nothing")
        print("4. Flee")
        print("> ", end=' ')
        raw_input = input()
        print("\n________________________________________________________________________________________________\n")
        if raw_input == "1":
            # Player attacks enemy
            player.attack(enemy)
            if enemy.health <= 0:
                print(f"The {enemy.race} is dead.")
            if Helper.is_zombie(): # enemy is a zombie and it can't be killed. 
                enemy.undead()
                if count == 3:
                    print("\nThis zombie doesn't seem to be taking damage! What should we do?")
                    count = 0
        elif raw_input == "2":
            player.spy(enemy)
            print()
        elif raw_input == "3":
            pass
        elif raw_input == "4":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")
        if enemy.health > 0:
            # Enemy attacks hero
            import rpg_classes
            # Hero = rpg_classes.Hero
            # Medic = rpg_classes.Medic
            # Rogue = rpg_classes.Rogue
            if isinstance(player, Hero):
                enemy.attack(player)
            if isinstance(player, Medic):
                player.heal()
                enemy.attack(player)
            if isinstance(player, Rogue):
                if player.chance_evade():
                    enemy.rogue_evade_attack(player)
                else:
                    enemy.attack(player)
            if player.health <= 0:
                print(f"{player.name} is dead.")
        combat_turn += 1
