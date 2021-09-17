from random import *

#todo function for random health


#todo function for random attack power


#todo function for randomizing enemy


#todo function for character creation

#todo combat options differ depending on the type of player character

#todo have player races differ in some way?


def chance(num1 = 1, num2 = 20):
    x = randint(num1, num2)
    return x

#* dice rolling function
def rolld(num = 20):
    roll = randint(1, num)
    return roll

#* roll to hit function
def roll_to_hit(attacker, target):
    roll = randint(1, 20)
    did_hit = (roll + attacker.to_hit) >= target.armor 
    print(f"attacker's roll: {roll + attacker.to_hit} >= target's armor: {target.armor}")
    print(did_hit)
    return did_hit




