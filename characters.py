# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 23:17:10 2024

@author: Francesco Brandoli
"""
from weapons import * 
from spells import *
from Prehistoric_functions import *



class Character:
    def __init__(self, name, attack, defense, pf):
        self.name = name
        self.title = []
        self.level = 1
        self.experience = 0
        self.weapon = None
        self.item = None
        self.attack = attack
        self.defense = defense
        self.pf = pf

    def __str__(self):
        return (f"Name: {self.name}, Level: {self.level}, Experience: {self.experience}, "
                f"Weapon: {self.weapon}, Item: {self.item}, Attack: {self.attack}, "
                f"Defense: {self.defense}, PF: {self.pf}")

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def equip_item(self, item):
        self.item = item

    def gain_experience(self, experience):
        self.experience += experience
        
    def gain_title(self, title):
        self.title.append(title)

    def level_up(self, new_level, attack, defense, pf):
        self.level += new_level
        self.attack += attack
        self.defense += defense
        self.pf += pf

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 10, 10, 20)
        self.weapon = [Sword()]

    def level_up(self, new_level, attack, defense, pf):
        super().level_up(new_level, attack, defense, pf)
        self.attack += 1

class Hunter(Character):
    def __init__(self, name):
        super().__init__(name, 10, 5, 25)
        self.weapon = [Bow()]
    
    def level_up(self, new_level, attack, defense, pf):
        super().level_up(new_level, attack, defense, pf)
        self.defense += 1


class Shaman(Character):
    def __init__(self, name):
        super().__init__(name, 5, 5, 30)
        self.magic = [Fireball()]
        self.weapon = [Wand()]
        
    def level_up(self, new_level, attack, defense, pf):
        super().level_up(new_level, attack, defense, pf)
        self.pf += 1


    def __str__(self):
        return (super().__str__() + f", Magic: {self.magic}")
    
class Thief(Character):
    def __init__(self, name):
        super().__init__(name, 5, 10, 25)
        self.weapon = [Bow()]
    
    def level_up(self, new_level, attack, defense, pf):
        super().level_up(new_level, attack, defense, pf)
        self.defense += 1
        
character_classes = [Warrior, Hunter, Shaman, Thief]

def generate_random_character():
    random_character_class = random.choice(character_classes)
    random_name = generate_name()
    random_character = random_character_class(random_name)
    print(f'There is a {random_character_class.__name__} in the forest!')
    return random_character



