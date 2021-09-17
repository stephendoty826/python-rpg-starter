from random import *

from rpg_functions import *

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self, race, name, health = 10, attack_power = 1, to_hit = -1, armor = 6):
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



class Hero(Character):
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

    def spy(self, target):
        print(f"{target.race} - HP: {target.health}, AC: {target.armor}")



class Medic(Character):
    def __init__(self, race, name, health = 10, attack_power = 2, to_hit = 0, armor = 8):
        super().__init__(race, name, health, attack_power, to_hit, armor)

    def heal(self):
        healing_chance = chance(1, 5)
        if healing_chance == 5:
            healing = chance(1, 3)
            self.health += healing
            print(f"{self.name} uses healing to regain {healing} HP!")
    # todo add first_add function
    # def first_aid(self):
    #     healing = chance()

    def spy(self, target):
        print(f"{target.name} - HP: {target.health}, AC: {target.armor}")






class Enemy:
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
            print(f"The {self.race} attacks and does {self.attack_power} damage to {target.name}.")
        else:
            print(f"The {self.race}'s attack misses.")
    
    def print_status(self):
        print(f"{self.name} - HP: {self.health}, Attack: {self.attack_power}, To-hit: {self.to_hit}, AC: {self.armor}")



class Goblin(Enemy):
    def __init__(self, race = "goblin", name = "Goblin", health = 7, attack_power = 2, to_hit = 0, armor = 9):
        super().__init__(race, name, health, attack_power, to_hit, armor)



class Zombie(Enemy):
    def __init__(self, race = "zombie", name = "Zombie", health = 50, attack_power = 1, to_hit = 0, armor = 6):
        super().__init__(race, name, health, attack_power, to_hit, armor)
        
    def undead(self):
        if self.health < 50:
            self.health = 50



class Shadow(Enemy):
    def __init__(self, race = "shadow", name = "Shadow", health = 1, attack_power = 4, to_hit = 3, armor = 18):
        super().__init__(race, name, health, attack_power, to_hit, armor)

    # def evade(self):
    #     pass