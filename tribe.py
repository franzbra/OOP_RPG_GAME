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
            
    def consume_food(self):    
        if 'Meat' in self.cumulative_items and self.cumulative_items['Meat'] > 0:
            for member in self.characters:
                if self.cumulative_items['Meat'] > 0:
                    self.cumulative_items['Meat'] -= 1
                    print(f"{member.name} consumed 1 unit of Food.")
                    print(f"Remaining Food: {self.cumulative_items['Meat']}")
                else:
                    print(f"{member.name} has no Food to consume.")
                    tribe.remove_member(member)
        else:
            print("There's no Food available in the tribe's inventory.")
            game_over = True
            return game_over
    
        self.display_cumulative_items()
        
    def remove_member(self, member):
        if member in self.characters:
            self.characters.remove(member)
            self.update_cumulative_items()
            print(f"{member.name} is dead!")

