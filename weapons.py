# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 23:14:55 2024

@author: Francesco Brandoli
"""

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return f"{self.name} (Damage: {self.damage})"

class Sword(Weapon):
    def __init__(self):
        super().__init__("Sword", 10)

class Wand(Weapon):
    def __init__(self):
        super().__init__("Wand", 5)

class Bow(Weapon):
    def __init__(self):
        super().__init__("Bow", 8)

class Dagger(Weapon):
    def __init__(self):
        super().__init__("Dagger", 6)
        
class Axe(Weapon):
    def __init__(self):
        super().__init__("Axe", 12)

