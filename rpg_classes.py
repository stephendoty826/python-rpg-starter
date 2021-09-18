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

# class Fighter(Player):                   # class Goblin(Enemy):

class Character:
    def __init__(self, race, name, health, attack_power, to_hit, armor):
        self.race = race
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.to_hit = to_hit
        self.armor = armor

    def attack(self, target):
        roll = randint(1, 20)
        if (roll + self.to_hit) >= target.armor:
            if isinstance(self, Player):
                print(f"HIT! {self.name} rolled a {roll + self.to_hit} which hits the {target.race}, dealing {self.attack_power} damage.\n")
            else:
                print(f"HIT! The {self.race} rolled a {roll + self.to_hit} which hits {target.name}, dealing {self.attack_power} damage.\n")
            target.health -= self.attack_power
            return True
        else:
            if isinstance(self, Player):
                print(f"MISS! {self.name} rolled a {roll + self.to_hit} which misses {target.race}.\n")
            else:
                print(f"MISS! The {self.race} rolled a {roll + self.to_hit} which misses {target.name}.\n")
            return False
    
    def alive(self):
        alive = True
        if self.health <= 0:
            alive = False
        return alive

    def print_status(self):
        print(f"{self.name} - HP: {self.health}, Attack: {self.attack_power}, To-hit: {self.to_hit}, AC: {self.armor}")






class Player(Character):
    def __init__(self, race, name, health, attack_power, to_hit, armor):
        super().__init__(race, name, health, attack_power, to_hit, armor)
        #todo add special ability points

    def spy(self, enemy):
        print(f"{self.name} uses spy on the {enemy.race} - HP: {enemy.health}, AC: {enemy.armor}")



class Enemy(Character):
    def __init__(self, race, name, health, attack_power, to_hit, armor, bounty):
        super().__init__(race, name, health, attack_power, to_hit, armor)
        self.bounty = bounty

    #todo need to fix. roll_to_hit() was replaced with attack in Character class. Also redo wording to match other attacks. 
    def rogue_evade_attack(self, player):
        if Character.attack(self, player):
            print(f"{player.name} quickly dodges and only takes half-damage ({math.trunc(self.attack_power/2)})\n.")
            player.health += round(self.attack_power/2)






class Fighter(Player):
    def __init__(self, race, name, health = 12, attack_power = 3, to_hit = 1, armor = 10):
        super().__init__(race, name, health, attack_power, to_hit, armor)

    def attack(self, enemy):
        roll = randint(1, 20)
        if (roll + self.to_hit) >= enemy.armor:
            crit_chance = randint(1, 5)
            if crit_chance == 5:
                enemy.health -= self.attack_power * 2
                print(f"HIT! {self.name} rolled a {roll + self.to_hit} which hits the {enemy.race}. {self.name}'s sword strikes true dealing {self.attack_power * 2} damage.\n")
            else:
                enemy.health -= self.attack_power
                print(f"HIT! {self.name} rolled a {roll + self.to_hit} which hits the {enemy.race}, dealing {self.attack_power} damage.\n")
        else:
            print(f"MISS! {self.name} rolled a {roll + self.to_hit} which misses the {enemy.race}.\n")

    #todo: add auto crit attack which takes special ability points...



class Medic(Player):
    def __init__(self, race, name, health = 10, attack_power = 2, to_hit = 0, armor = 8):
        super().__init__(race, name, health, attack_power, to_hit, armor)

    def heal(self):
        healing_chance = randint(1, 5)
        if healing_chance == 5:
            healing = randint(1, 3)
            self.health += healing
            print(f"{self.name} uses healing to regain {healing} HP!\n")

    # todo add first_add function which takes special ability points...
    # def first_aid(self):
    #     healing = chance()



class Rogue(Player):
    def __init__(self, race, name, health = 8, attack_power = 2, to_hit = 3, armor = 9):
        super().__init__(race, name, health, attack_power, to_hit, armor)

    def chance_evade(self):
        evade_chance = randint(1,5)
        if evade_chance == 5:
            return True
        else: 
            return False

    # todo add first_add function which takes special ability points...
    # def first_aid(self):
    #     healing = chance()






class Goblin(Enemy):
    def __init__(self, race = "goblin", name = "Goblin", health = randint(6, 8), attack_power = randint(2, 3), to_hit = randint(0, 1), armor = randint(8, 10), bounty = 5):
        super().__init__(race, name, health, attack_power, to_hit, armor, bounty)

    #todo: add special abilities (critical hit) that can run "randomly" (1 in 8) per battle

class Zombie(Enemy):
    def __init__(self, race = "zombie", name = "Zombie", health = randint(20, 25), attack_power = randint(1, 2), to_hit = randint(-2, -1), armor = randint(6, 8), bounty = 15):
        super().__init__(race, name, health, attack_power, to_hit, armor, bounty)
        
    def undead(self):
        if self.health <= 0:
            self.health = 25

    #todo: add special abilities (bite that poisons you and you take 1 damage for 3 turns) that can run "randomly" (1 in 8) per battle  

class Shadow(Enemy):
    def __init__(self, race = "shadow", name = "Shadow", health = randint(1, 3), attack_power = randint(3, 5), to_hit = randint(4, 5), armor = randint(18, 19), bounty = 8):
        super().__init__(race, name, health, attack_power, to_hit, armor, bounty)
    
    #todo: add special abilities (something that skips your turn?) that can run "randomly" (1 in 8) per battle

class Fire_Serpent(Enemy):
    def __init__(self, race = "fire serpent", name = "Fire Serpent", health = randint(16, 18), attack_power = randint(3, 4), to_hit = randint(2, 3), armor = randint(12, 14), bounty = 30):
        super().__init__(race, name, health, attack_power, to_hit, armor, bounty)

    #todo: add special abilities (firebreath that does 3x damage and 1 damage per turn for 3 turns) that can run "randomly" (1 in 5) per battle


#todo add more enemies (use dnd monsters for ideas)




class SuperTonic:
    def __init__(self, name = "Super Tonic", in_inventory = 0):
        self.name = name
        self.in_inventory = in_inventory

    def use_tonic(self, player):
        player.health += randint(1, 4) * 2 + 4



class Helper:
        
    def is_fighter(player):
        return isinstance(player, Fighter)

    def is_medic(player):
        return isinstance(player, Medic)

    def is_rogue(player):
        return isinstance(player, Rogue)

    def is_goblin(enemy):
        return isinstance(enemy, Goblin)

    def is_zombie(enemy):
        return isinstance(enemy, Zombie)

    def is_shadow(enemy):
        return isinstance(enemy, Shadow)

    def is_fire_serpent(enemy):
        return isinstance(enemy, Fire_Serpent)




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