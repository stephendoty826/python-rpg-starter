from rpg_battle import *

from rpg_town import *

# store = [Helper.SuperTonic]

# store_description = {
#     "Super Tonic": "A tonic that restores 10 HP. Can be used in battle."
#     }



print()

while True:
    print("What do you want to do?")
    print("1. Fight a monster.")
    print("2. Go to town.")
    print("3. Quit.")
    # print("3. Explore.")
    print("> ", end = ' ')
    raw_input = input()
    print("________________________________________________________________________________________________\n")
    if raw_input == "1":
        # choose enemy function
        battle(fighter, goblin)
    elif raw_input == "2":
        town(fighter)
    elif raw_input == "3":
        print("Thanks for playing.\n")
        break
    else:
        print(f"Invalid input {raw_input}")



#todo have shop with option to view info of item. 