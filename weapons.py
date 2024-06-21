# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 23:14:55 2024

@author: Francesco Brandoli
"""

class Weapon:
    def __init__(self, name, damage, precision):
        self.name = name
        self.damage = damage
        self.expertise = 10
        self.precision = precision

    def __str__(self):
        return f"{self.name} (Damage: {self.damage})"

class Sword(Weapon):
    def __init__(self):
        super().__init__("Sword", 10, 20)

class Wand(Weapon):
    def __init__(self):
        super().__init__("Wand", 5, 20)

class Bow(Weapon):
    def __init__(self):
        super().__init__("Bow", 8, 30)

class Dagger(Weapon):
    def __init__(self):
        super().__init__("Dagger", 6, 30)
        
class Axe(Weapon):
    def __init__(self):
        super().__init__("Axe", 12, 20)
        
weapons_classes = {
    'Sword': Sword,
    'Wand': Wand,
    'Bow': Bow,
    'Dagger': Dagger,
    'Axe': Axe
}
