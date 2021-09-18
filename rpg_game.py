# from rpg_classes import *
import rpg_classes

Fighter = rpg_classes.Fighter
Medic = rpg_classes.Medic
Rogue = rpg_classes.Rogue
Goblin = rpg_classes.Goblin
Zombie = rpg_classes.Zombie
Shadow = rpg_classes.Shadow
Fire_Serpent = rpg_classes.Fire_Serpent
Helper = rpg_classes.Helper

from rpg_battle import *

from rpg_functions import *

# store = [Helper.SuperTonic]

# store_description = {
#     "Super Tonic": "A tonic that restores 10 HP. Can be used in battle."
#     }

human_fighter = Fighter("human", "Baden", health = 50)

dwarven_medic = Medic("dwarf", "Thigrel", health = 50)

elven_rogue = Rogue("elven", "Khiiral", health = 50)

goblin = Goblin(name = "Goblin", health = 25)

zombie = Zombie(name = "Zombie")

shadow = Shadow(name = "Shadow")

fire_serpent = Fire_Serpent(name = "Fire Serpent")

print()

while True:
    print("What do you want to do?")
    print("1. Fight a monster.")
    print("2. Go to town.")
    print("3. Quit.")
    # print("3. Explore.")
    print("> ", end=' ')
    raw_input = input()
    if raw_input == "1":
        battle(human_fighter, goblin)
    elif raw_input == "2":
        # go to town
        pass
    elif raw_input == "3":
        print("Thanks for playing.")
        break
    else:
        print(f"Invalid input {raw_input}")



#todo have shop with option to view info of item. 