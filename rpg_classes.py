import math

from random import *

from rpg_functions import *

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

#todo add OnePunchMan class that kills everything in 1 hit (make his attack power "over 9000" and print out something referring to that) and can't die



                        # class Character:

# class Player(Character):              # class Enemy(Character):

# class Hero(Player):                   # class Zombie(Enemy):

class Character:
    def __init__(self, race, name, health, attack_power, to_hit, armor):
        self.race = race
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.to_hit = to_hit
        self.armor = armor


    def alive(self):
        alive = True
        if self.health <= 0:
            alive = False
        return alive
    
    def attack(self, target):
        if roll_to_hit(self, target):
            target.health -= self.attack_power
            print(f"{self.name} attacks and does {self.attack_power} damage to the {target.name}.")
        else:
            print(f"{self.name}'s attack misses.")
    
    def print_status(self):
        print(f"{self.name} - HP: {self.health}, Attack: {self.attack_power}, To-hit: {self.to_hit}, AC: {self.armor}")






class Player(Character):
    def __init__(self, race, name, health, attack_power, to_hit, armor):
        super().__init__(race, name, health, attack_power, to_hit, armor)
        #todo add special ability points

    def spy(self, target):
        print(f"{target.race} - HP: {target.health}, AC: {target.armor}")



class Hero(Player):
    def __init__(self, race, name, health = 12, attack_power = 3, to_hit = 1, armor = 10):
        super().__init__(race, name, health, attack_power, to_hit, armor)

    def attack(self, target):
        if roll_to_hit(self, target):
            crit_chance = chance(1, 5)
            if crit_chance == 5:
                target.health -= self.attack_power * 2
                print(f"CRITICAL HIT! The {self.name} strikes hard dealing {self.attack_power * 2} damage to the {target.race}.")
            else:
                target.health -= self.attack_power
                print(f"{self.name} attacks and does {self.attack_power} damage to the {target.race}.")
        else:
            print(f"{self.name}'s attack misses.")

    #todo: add auto crit attack which takes special ability points...



class Medic(Player):
    def __init__(self, race, name, health = 10, attack_power = 2, to_hit = 0, armor = 8):
        super().__init__(race, name, health, attack_power, to_hit, armor)

    def heal(self):
        healing_chance = chance(1, 5)
        if healing_chance == 5:
            healing = chance(1, 3)
            self.health += healing
            print(f"{self.name} uses healing to regain {healing} HP!")

    # todo add first_add function which takes special ability points...
    # def first_aid(self):
    #     healing = chance()



class Rogue(Player):
    def __init__(self, race, name, health = 8, attack_power = 2, to_hit = 3, armor = 9):
        super().__init__(race, name, health, attack_power, to_hit, armor)

    def chance_evade(self):
        evade_chance = chance(1, 5)
        print(f"evade chance = {evade_chance}")
        if evade_chance == 5:
            return True
        else: 
            return False

    # todo add first_add function which takes special ability points...
    # def first_aid(self):
    #     healing = chance()






class Enemy(Character):
    def __init__(self, race, name, health, attack_power, to_hit, armor):
        super().__init__(race, name, health, attack_power, to_hit, armor)

    def rogue_evade_attack(self, target):
        if roll_to_hit(self, target):
            target.health -= math.trunc(self.attack_power/2)
            print(f"The {self.race} attacks and does {self.attack_power} damage to {target.name}.")
            print(f"{target.name} evades and takes half-damage ({math.trunc(self.attack_power/2)}).")
        else:
            print(f"The {self.race}'s attack misses.")



class Goblin(Enemy):
    def __init__(self, race = "goblin", name = "Goblin", health = 7, attack_power = 2, to_hit = 0, armor = 9, bounty = 5):
        super().__init__(race, name, health, attack_power, to_hit, armor, bounty)

    #todo: add special abilities (critical hit) that can run "randomly" (1 in 8) per battle

class Zombie(Enemy):
    def __init__(self, race = "zombie", name = "Zombie", health = 50, attack_power = 1, to_hit = -2, armor = 6, bounty = 15):
        super().__init__(race, name, health, attack_power, to_hit, armor, bounty)
        
    def undead(self):
        if self.health < 50:
            self.health = 50

    #todo: add special abilities (bite that poisons you and you take 1 damage for 3 turns) that can run "randomly" (1 in 8) per battle  

class Shadow(Enemy):
    def __init__(self, race = "shadow", name = "Shadow", health = 1, attack_power = 4, to_hit = 3, armor = 18, bounty = 8):
        super().__init__(race, name, health, attack_power, to_hit, armor, bounty)
    
    #todo: add special abilities (something that skips your turn?) that can run "randomly" (1 in 8) per battle

class Fire_Serpent(Enemy):
    def __init__(self, race = "fire serpent", name = "Fire Serpent", health = 16, attack_power = 3, to_hit = 2, armor = 13, bounty = 30):
        super().__init__(race, name, health, attack_power, to_hit, armor, bounty)

    #todo: add special abilities (firebreath that does 3x damage and 1 damage per turn for 3 turns) that can run "randomly" (1 in 5) per battle


#todo add more enemies (use dnd monsters for ideas)




class SuperTonic:
    def __init__(self, name = "Super Tonic", in_inventory = 0):
        self.name = name
        self.in_inventory = in_inventory

    def use_tonic(self, player):
        player.health += rolld(4) * 2 + 4



class Helper:
    def roll_to_hit(attacker, target):
        roll = randint(1, 20)
        print(roll)
        if (roll + attacker.to_hit) >= target.armor:
            if isinstance(attacker, Hero) or isinstance(attacker, Medic) or isinstance(attacker, Rogue):
                print(f"{attacker.name} is a Character")
                print(f"{attacker.name} rolled a {roll + attacker.to_hit} which hits {target.name}'s armor of {target.armor}")
            else:
                print(f"The {attacker.race} rolled a {roll + attacker.to_hit} which hits {target.name}'s armor of {target.armor}")
            return True
        else:
            if isinstance(attacker, Hero) or isinstance(attacker, Medic) or isinstance(attacker, Rogue):
                print(f"{attacker.name} is a Character")
                print(f"{attacker.name} rolled a {roll + attacker.to_hit} which misses {target.name}'s armor of {target.armor}")
            else:
                print(f"The {attacker.race} rolled a {roll + attacker.to_hit} which misses {target.name}'s armor of {target.armor}")
        
    def is_zombie(monster):
        return isinstance(monster, Zombie)




super_tonic = SuperTonic()
item2 = SuperTonic(name = "item2")
item3 = SuperTonic(name = "item3")

health = 5

inventory = [super_tonic, item2, item3]

def use_item():
    if inventory != []:
        print("Which item would you like to use?")
        for item in inventory:
            print(f"{inventory.index(item) + 1}.{item.name}")
        input()

# use_item()