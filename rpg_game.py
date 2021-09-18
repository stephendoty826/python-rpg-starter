# from rpg_classes import *
import rpg_classes

Fighter = rpg_classes.Fighter
Medic = rpg_classes.Medic
Rogue = rpg_classes.Rogue
Goblin = rpg_classes.Goblin
Zombie = rpg_classes.Zombie
Shadow = rpg_classes.Shadow
Fire_Serpent = rpg_classes.Fire_Serpent

from rpg_battle import *

from rpg_functions import *

human_fighter = Fighter("human", "Baden", health = 50)

dwarven_medic = Medic("dwarf", "Thigrel", health = 50)

elven_rogue = Rogue("elven", "Khiiral", health = 50)

goblin = Goblin(name = "Goblin")

zombie = Zombie(name = "Zombie")

shadow = Shadow(name = "Shadow")

fire_serpent = Fire_Serpent(name = "Fire Serpent")

battle(human_fighter, fire_serpent)

# roll_to_hit(elven_rogue, goblin)


#todo You can kill a zombie using fire. Have info in shop about how firebomb can be used to burn dead bodies. 

#todo have shop with option to view info of item. 