# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 00:06:10 2024

@author: Francesco Brandoli
"""
import random

class Menu:
    def __init__(self, character):
        self.character = character

    def attack(self, monster):
        # Simulate an attack action
        print(f"{self.character.name} attacks {monster.__class__.__name__}!")

        # Calculate damage based on character's attack and monster's defense
        damage = (self.character.attack)
        monster.pf -= damage

        # Check if the monster is defeated
        if monster.pf <= 0:
            print(f"{monster.name} is defeated!")
            self.character.gain_experience(monster.experience)
            return True
        else:
            print(f"{monster.name} has {monster.pf} PF remaining.")
            return False

    def flight(self):
        # Simulate a flight action
        print(f"{self.character.name} attempts to flee.")

        # Determine success based on random chance
        if random.random() < 0.5:
            print("Flee successful!")
            return True
        else:
            print("Flee unsuccessful. Prepare for the next attack!")
            return False

    def craft(self):
        # Simulate a crafting action
        print(f"{self.character.name} is crafting items or weapons.")

        # Logic for crafting can be added here
        print("Crafting completed.")
    
    def rest(self):
        # Simulate a rest action
        print(f"{self.character.name} is resting to regain strength.")

        # Add logic to regain health or other attributes
        self.character.pf+self.character.level
        print("Resting completed.")
        
    def open_menu(self, monster):
        print('What do you want to do?')
        choice = int(input('1) Fight\n2) Flight\n3) Craft\n4) Rest\n'))

        if choice == 1:
            # Call attack method
            self.attack(monster)
        elif choice == 2:
            # Call flight method
            self.flight()
        elif choice == 3:
            # Call craft method
            self.craft()
        elif choice == 4:
            # Call rest method
            self.rest()
