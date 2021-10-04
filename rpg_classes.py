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
        self.max_hp = self.health

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
        print(f"{self.name} - HP: {self.health}, Attack: {self.attack_power}, To-hit: {self.to_hit}, AC: {self.armor}\n")



class Player(Character):
    def __init__(self, race, name, health, attack_power, to_hit, armor, has_bug, coin_purse = 0, inventory = [], current_bounty = []):
        super().__init__(race, name, health, attack_power, to_hit, armor)
        #todo add special ability points
        self.has_bug = has_bug
        self.coin_purse = coin_purse
        self.inventory = inventory
        self.current_bounty = current_bounty


    def spy(self, enemy):
        print(f"{self.name} uses spy on the {enemy.race} - HP: {enemy.health}, AC: {enemy.armor}\n")


class Enemy(Character):
    def __init__(self, race, name, health, attack_power, to_hit, armor, bounty, is_specialty_bounty):
        super().__init__(race, name, health, attack_power, to_hit, armor)
        self.bounty = bounty
        self.is_specialty_bounty = is_specialty_bounty

    #todo need to fix. roll_to_hit() was replaced with attack in Character class. Also redo wording to match other attacks. 
    def rogue_evade_attack(self, player):
        if Character.attack(self, player):
            print(f"{player.name} quickly dodges and only takes half-damage ({math.trunc(self.attack_power/2)})\n.")
            player.health += round(self.attack_power/2)



class Fighter(Player):
    def __init__(self, race, has_bug = False, name = "Fighter", health = 13, attack_power = 3, to_hit = 3, armor = 10, is_evading = False):
        super().__init__(race, name, health, attack_power, to_hit, armor, has_bug, coin_purse = 0)
        self.is_evading = is_evading

    def attack(self, enemy):
        roll = randint(1, 20)
        if (roll + self.to_hit) >= enemy.armor:
            crit_chance = randint(1, 4)
            if crit_chance == 4:
                enemy.health -= self.attack_power * 2
                print(f"HIT! {self.name} rolled a {roll + self.to_hit} which hits the {enemy.race}. {self.name}'s sword strikes true dealing {self.attack_power * 2} damage.\n")
            else:
                enemy.health -= self.attack_power
                print(f"HIT! {self.name} rolled a {roll + self.to_hit} which hits the {enemy.race}, dealing {self.attack_power} damage.\n")
        else:
            print(f"MISS! {self.name} rolled a {roll + self.to_hit} which misses the {enemy.race}.\n")

    #todo: add auto crit attack which takes special ability points...


class Medic(Player):
    def __init__(self, race, has_bug = False, name = "Medic", health = 11, attack_power = 3, to_hit = 2, armor = 9, is_evading = False):
        super().__init__(race, name, health, attack_power, to_hit, armor, has_bug, coin_purse = 0)
        self.is_evading = is_evading

    def heal(self):
        healing_chance = randint(1, 4)
        if healing_chance == 4:
            healing = randint(2, 3)
            self.health += healing
            print(f"{self.name} uses healing to regain {healing} HP!\n")

    # todo add first_add function which takes special ability points...
    # def first_aid(self):
    #     healing = chance()


class Rogue(Player):
    def __init__(self, race, has_bug = False, name = "Rogue", health = 12, attack_power = 3, to_hit = 5, armor = 8, is_evading = False):
        super().__init__(race, name, health, attack_power, to_hit, armor, has_bug, coin_purse = 0)
        self.is_evading = is_evading

    def chance_evade(self):
        evade_chance = randint(1, 4)
        if evade_chance == 4:
            return True
        else: 
            return False

    # todo add first_add function which takes special ability points...
    # def first_aid(self):
    #     healing = chance()



class Goblin(Enemy):
    def __init__(self, race = "goblin", name = "Goblin", health = randint(7, 8), attack_power = randint(2, 3), to_hit = randint(0, 1), armor = randint(7, 8), bounty = 3, is_specialty_bounty = False):
        super().__init__(race, name, health, attack_power, to_hit, armor, bounty, is_specialty_bounty)

    #todo: add special abilities (critical hit) that can run "randomly" (1 in 8) per battle


class Zombie(Enemy):
    def __init__(self, race = "zombie", name = "Zombie", health = randint(12, 16), attack_power = randint(1, 2), to_hit = randint(0, 1), armor = randint(5, 7), bounty = 15, is_specialty_bounty = False):
        super().__init__(race, name, health, attack_power, to_hit, armor, bounty, is_specialty_bounty)

    def undead(self):
        if self.health <= 0:
            self.health = self.max_hp

    #todo: add special abilities (bite that poisons you and you take 1 damage for 3 turns) that can run "randomly" (1 in 8) per battle  


class Shadow(Enemy):
    def __init__(self, race = "shadow", name = "Shadow", health = randint(1, 2), attack_power = randint(3, 4), to_hit = randint(5, 6), armor = randint(17, 18), bounty = 6, is_specialty_bounty = False):
        super().__init__(race, name, health, attack_power, to_hit, armor, bounty, is_specialty_bounty)
    
    #todo: add special abilities (something that skips your turn?) that can run "randomly" (1 in 8) per battle


class Fire_Serpent(Enemy):
    def __init__(self, race = "fire serpent", name = "Fire Serpent", health = randint(18, 20), attack_power = randint(4, 5), to_hit = randint(2, 3), armor = randint(11, 13), bounty = 30, is_specialty_bounty = False):
        super().__init__(race, name, health, attack_power, to_hit, armor, bounty, is_specialty_bounty)

    #todo: add special abilities (firebreath that does 3x damage and 1 damage per turn for 3 turns) that can run "randomly" (1 in 5) per battle


class Troll(Enemy):
    def __init__(self, race = "troll", name = "Troll", health = randint(25, 30), attack_power = randint(6, 7), to_hit = randint(-3, -1), armor = randint(4, 5), bounty = 10, is_specialty_bounty = False):
        super().__init__(race, name, health, attack_power, to_hit, armor, bounty, is_specialty_bounty)
#todo add more enemies (use dnd monsters for ideas)


# Store reusable items
class Super_Tonic:
    def __init__(self, name = "Super Tonic", description = "restores (11 - 14) HP", price = 12):
        self.name = name
        self.description = description
        self.price = price

    def use(self, player, enemy):
        regen = randint(1, 4) + 10
        if regen + player.health > player.max_hp:
            player.health = player.max_hp
            print(f"{player.name} uses Super Tonic and is back at Max HP.")
        else:
            player.health += regen
            print(f"{player.name} uses Super Tonic and regains {regen} HP.")


class Firebomb:
    def __init__(self, name = "Firebomb", description = "deals (6 - 9) fire damage", price = 8):   
        self.name = name
        self.description = description
        self.price = price

    def use(self, player, enemy):
        roll = randint(1, 20)
        if (roll + player.to_hit) >= enemy.armor:
            if Helper.is_goblin(enemy) or Helper.is_shadow(enemy) or Helper.is_troll(enemy):
                damage = randint(1, 4) + 5
                enemy.health -= damage
                print(f"HIT! {player.name} rolls a {roll + player.to_hit} and throws the firebomb, landing a direct hit. The {enemy.race} \ncries out in pain as it takes {damage} fire damage.\n")
            if Helper.is_zombie(enemy):
                enemy.health = 0
                print(f"HIT! {player.name} rolls a {roll + player.to_hit} and throws the firebomb, landing a direct hit. The zombie is \nquickly engulfed in flames and topples to the ground.\n")
            if Helper.is_fire_serpent(enemy):
                regen = randint(1, 6) + 6
                enemy.health += regen
                print(f"HIT! {player.name} rolls a {roll + player.to_hit} and throws the firebomb, landing a direct hit. The fire \nserpent laps up the fire and regains {regen} HP.\n")
        else:
            if Helper.is_goblin(enemy) or Helper.is_shadow(enemy) or Helper.is_troll(enemy):
                print(f"MISS! {player.name} rolls a {roll + player.to_hit} and throws the firebomb, missing. The firebomb explodes into \nflames behind the {enemy.race} cause no damage.\n")
            if Helper.is_fire_serpent(enemy):
                print(f"MISS! {player.name} rolls a {roll + player.to_hit} and throws the firebomb, missing. The fire serpent easily \nslithers right through the flames and prepares for an attack.\n")
            if Helper.is_zombie(enemy):
                print(f"MISS! {player.name} rolls a {roll + player.to_hit} and throws the firebomb, missing by a hair. The firebomb \nexplodes into flames just behind the zombie noticeably damaging it's feet. You're sure if you can land a hit with a \nfirebomb, you can kill this thing.\n")


class Evade:
    def __init__(self, name = "Evade", description = "temporarily increases AC by 4 (2 turns)", price = 10):   
        self.name = name
        self.description = description
        self.price = price

    def use(self, player, enemy):
        player.is_evading = True


class Water_Balloon:
    def __init__(self, name = "Water Balloon", description = "just what it sounds like...a balloon filled with water", price = 1):   
        self.name = name
        self.description = description
        self.price = price

    def use(self, player, enemy):
        roll = randint(1, 20)
        if (roll + player.to_hit) >= enemy.armor:
            if Helper.is_goblin(fire_serpent):
                damage = randint(1, 4) + 4
                enemy.health -= damage
                print(f"HIT! {player.name} rolls a {roll + player.to_hit} and throws the water balloon, landing a direct hit. The {enemy.race} \ncries out in pain as it takes {damage} water damage.\n")
            else:
                print(f"HIT! {player.name} rolls a {roll + player.to_hit} and throws the water balloon, landing a direct hit. Your attack \ndoes no damage. The {enemy.race} is now wet and looks very annoyed.")
        else:
            print(f"MISS! {player.name} rolls a {roll + player.to_hit} and throws the water balloon, missing.")


# Store Upgrades
class AC_Upgrade:
    def __init__(self, name = "AC Upgrade", description = "permanently increases AC by 2", price = 20):   
        self.name = name
        self.description = description
        self.price = price

    def use(self, player):
        player.armor += 2
        print(f"{player.name}'s armor has increase to {player.armor}. You now have {player.coin_purse} gold.\n")


class HP_Upgrade:
    def __init__(self, name = "HP Upgrade", description = "permanently increases max HP by 4", price = 20):   
        self.name = name
        self.description = description
        self.price = price

    def use(self, player):
        player.health += 4
        print(f"{player.name}'s health has increase to {player.health}. You now have {player.coin_purse} gold.\n")

class To_Hit_Upgrade:
    def __init__(self, name = "To-Hit Upgrade", description = "permanently increases hit chance by 2", price = 20):   
        self.name = name
        self.description = description
        self.price = price

    def use(self, player):
        player.to_hit += 2
        print(f"{player.name}'s hit chance has increase to {player.to_hit}. You now have {player.coin_purse} gold.\n")

class Greataxe:
    def __init__(self, name = "Greataxe", description = "permanently increases attack power by 2", price = 20):   
        self.name = name
        self.description = description
        self.price = price

    def use(self, player):
        player.attack_power += 2
        print(f"{player.name}'s attack power has increase to {player.attack_power}. You now have {player.coin_purse} gold.\n")

class Bug_in_Bottle:
    def __init__(self, name = "Bug in a Bottle", description = "interesting looking bug in a bottle", price = 3):   
        self.name = name
        self.description = description
        self.price = price

    def use(self, player):
        player.has_bug = True
        print("You purchased the interesting looking bug in a bottle.\n")

#todo add weapon that increases attack power by 2. Make it fairly expensive.

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

    def is_troll(enemy):
        return isinstance(enemy, Troll)


# creatings standard bounties

# currently you can only fight one of each standard bounty? 
goblin = Goblin()
shadow = Shadow()
troll = Troll()

# creating specialty bounties
mudmug = Goblin(name = "Mudmug", health = randint(10, 11), attack_power = randint(3, 4), bounty = 6, is_specialty_bounty = True)
stigg = Goblin(name = "Stigg", health = randint(13, 14), to_hit =  randint(2, 3), bounty = 7, is_specialty_bounty = True)
undead_ned = Zombie(name = "Undead Ned", is_specialty_bounty = True)
big_nellie = Troll(name = "Big Nellie", health = randint(30, 35), attack_power = randint(8, 9), to_hit = randint(-1, 1), bounty = 20, is_specialty_bounty = True)
lighthouse_shadow = Shadow(name = "Shadow of the Lighthouse", health = randint(3, 4), attack_power = randint(4, 5), armor = randint(18, 19), bounty = 15, is_specialty_bounty = True)
fire_serpent = Fire_Serpent(is_specialty_bounty = True)

# couldn't choose fire_serpent as specialty bounty

# creating standard shop items
super_tonic = Super_Tonic()
firebomb = Firebomb()
evade = Evade()
water_balloon = Water_Balloon()

# creating specialty shop items
ac_upgrade = AC_Upgrade()
hp_upgrade = HP_Upgrade()
to_hit_upgrade = To_Hit_Upgrade()
greataxe = Greataxe()
bug_in_bottle = Bug_in_Bottle()

player = Fighter(race = "human")

enemy = Goblin()

evade.use(player, enemy)