# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 23:15:35 2024

@author: Francesco Brandoli
"""

class Spell:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return f"{self.name} (Damage: {self.damage})"

class Fireball(Spell):
    def __init__(self):
        super().__init__("Fireball", 30)
