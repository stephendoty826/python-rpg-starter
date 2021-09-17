# from rpg_classes import *
import rpg_classes

Hero = rpg_classes.Hero
Medic = rpg_classes.Medic
Rogue = rpg_classes.Rogue
Goblin = rpg_classes.Goblin
Zombie = rpg_classes.Zombie
Shadow = rpg_classes.Shadow
Fire_Serpent = rpg_classes.Fire_Serpent


from rpg_battle import *

from rpg_functions import *

human_hero = Hero("human", "Hero", health = 30)

dwarven_medic = Medic("dwarf", "Medic", health = 30)

elven_rogue = Rogue("elven", "Rogue", health = 30)

goblin = Goblin(health = 24)

zombie = Zombie()

shadow = Shadow()

battle(elven_rogue, goblin)

# roll_to_hit(elven_rogue, goblin)


#todo You can kill a zombie using fire. Have info in shop about how firebomb can be used to burn dead bodies. 

#todo have shop with option to view info of item. 