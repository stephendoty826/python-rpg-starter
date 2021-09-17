from rpg_classes import *

from rpg_battle import *

from rpg_functions import *

human_hero = Hero("human", "Hero", health = 30)

dwarven_medic = Medic("dwarf", "Medic", health = 30)

goblin = Goblin(health = 24)

zombie = Zombie()

shadow = Shadow()

battle(human_hero, shadow)

# roll_to_hit(human_hero, goblin)


#todo You can kill a zombie using fire. Have info in shop about how firebomb can be used to burn dead bodies. 

#todo have shop with option to view info of item. 