from random import *


# Goblin = rpg_classes.Goblin
# Zombie = rpg_classes.Zombie
# Shadow = rpg_classes.Shadow
# Fire_Serpent = rpg_classes.Fire_Serpent

#todo function for random health


#todo function for random attack power


#todo function for randomizing enemy


#todo function for character creation


#todo combat options differ depending on the type of player character


#todo have player races differ in some way (super special ability or other?)


def chance(num1 = 1, num2 = 20):
    roll = randint(num1, num2)
    return roll

#* dice rolling function
def rolld(num = 20):
    roll = randint(1, num)
    return roll


# def roll_to_hit(attacker, target):
#     roll = randint(1, 20)
#     print(roll)
#     if (roll + attacker.to_hit) >= target.armor:
#         print(f"The {attacker.race} rolled a {roll + attacker.to_hit} which hits {target.name}'s armor of {target.armor}")
#         return True
#     else:
#         print(f"The {attacker.race} rolled a {roll + attacker.to_hit} which misses {target.name}'s armor of {target.armor}")
#         return False




