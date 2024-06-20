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
        self.weapon = []
        self.item = {}
        self.attack = attack
        self.defense = defense
        self.pf = pf
        self.craft = 0
        self.communication = 0
        self.animal_affinity = 0
        self.search = 0

    def __str__(self):
        return (f"Name: {self.name}, Level: {self.level}, Experience: {self.experience}, "
                f"Weapon: {self.weapon}, Item: {self.item}, Attack: {self.attack}, "
                f"Defense: {self.defense}, PF: {self.pf}")

    def equip_weapon(self, weapon):
        self.weapon.append(weapon)

    def equip_item(self, item, quantity):
        if item in self.item:
            self.item[item] += quantity
        else:
            self.item[item] = quantity

    def gain_experience(self, experience):
        self.experience += experience
        if self.experience > 10*self.level :
            print(f"{self.name} is now stronger! New level = {self.level}")
            self.level_up()
            self.experience = self.experience - 10*self.level
        
    def gain_title(self, title):
        self.title.append(title)

    def level_up(self):
        self.level += 1
        self.attack += 1
        self.defense += 1
        self.pf += 1

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 10, 10, 20)
        self.weapon.append(Sword())

    def level_up(self):
        super().level_up()
        self.attack += 1

class Hunter(Character):
    def __init__(self, name):
        super().__init__(name, 10, 5, 25)
        self.weapon.append(Bow())
    
    def level_up(self):
        super().level_up()
        self.defense += 1


class Shaman(Character):
    def __init__(self, name):
        super().__init__(name, 5, 5, 30)
        self.magic = []
        self.magic.append(Fireball())
        self.weapon.append(Wand())
        
    def level_up(self):
        super().level_up()
        self.pf += 1


    def __str__(self):
        return (super().__str__() + f", Magic: {self.magic}")
    
class Thief(Character):
    def __init__(self, name):
        super().__init__(name, 5, 10, 25)
        self.weapon.append(Bow())
    
    def level_up(self):
        super().level_up()
        self.defense += 1
        
character_classes = [Warrior, Hunter, Shaman, Thief]

def generate_random_character():
    random_character_class = random.choice(character_classes)
    random_name = generate_name()
    random_character = random_character_class(random_name)
    print(f'There is a {random_character_class.__name__} in the forest!')
    return random_character



