# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 17:26:45 2024

@author: Francesco Brandoli
"""
from monsters import *

class Tribe:
    def __init__(self, name):
        self.characters = []
        self.cumulative_items = {}
        self.name = name

    def add_character(self, character):
        self.characters.append(character)
        self.update_cumulative_items()

    def update_cumulative_items(self):
        self.cumulative_items = {}
        for character in self.characters:
            if type(character) not in monster_classes:
                for item, quantity in character.item.items():
                    if item in self.cumulative_items:
                        self.cumulative_items[item] += quantity
                    else:
                        self.cumulative_items[item] = quantity

    def display_cumulative_items(self):
        print("Cumulative Items:")
        for item, quantity in self.cumulative_items.items():
            print(f"{item}: {quantity}")

    def display_characters(self):
        for character in self.characters:
            print(character.name, character.attack, character.defense)

