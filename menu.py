# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 00:06:10 2024

@author: Francesco Brandoli
"""
import random
from tribe import *

class Menu:
    def __init__(self, character,tribe):
        self.character = character
        self.tribe = tribe
        
    def select_weapon(self):
        if len(self.character.weapon) > 1:
            print("Choose a weapon:")
            for i, weapon in enumerate(self.character.weapon):
                print(f"{i + 1}) {weapon.name} (Expertise: {weapon.expertise})")
                weapon_choice = int(input()) - 1
        else:
            weapon_choice = 0
             
        selected_weapon = self.character.weapon[weapon_choice]
        return selected_weapon


    def attack(self, monster):
        # Simulate an attack action
        print(f"{self.character.name} attacks {monster.__class__.__name__}!")
        
        #Dynamic to hit the target
        selected_weapon = self.select_weapon()
        if selected_weapon.precision > monster.dexterity:
            selected_weapon.expertise += 1
            selected_weapon.precision += 1
            damage = (self.character.attack+selected_weapon.damage)
            monster.pf -= damage
            print(f"{monster.name} takes {damage} damage!")
        else : print(f"{monster.name} avoids the attack!")   

        # Check if the monster is defeated
        if monster.pf <= 0:
            print(f"{monster.name} is defeated!")
            self.character.gain_experience(monster.experience)
            for item, quantity in monster.item.items():
               if item in ["meat", "bones"]:
                   self.character.equip_item(item, quantity)
                   print(f"{self.character.name} obtains {quantity} {item} from {monster.name}.")                
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

    def tame(self, monster):
        #character try to tame the Monster
        print(f"{self.character.name} attempts to tame the {monster.name}")
        if self.character.animal_affinity >= monster.tamability:
            print(f"{monster.name} will now follow you!")
            self.tribe.add_character(monster)
            return True
        else : 
            print(f'{self.character.name}failed to tame the beast!')

    def craft(self):
        # Simulate a crafting action
        print(f"{self.character.name} is crafting items or weapons.")

        # Logic for crafting can be added here
        print("Crafting completed.")
    
    def rest(self, hours):
        # Simulate a rest action
        print(f"{self.character.name} rested for {hours} hours and gained {self.character.level*hours} pf")
        self.character.pf+=self.character.level*hours
        
    def train(self, hours):
        #simulate weapon or crafting training
        choice= int(input("What do you want to train?\n1)Weapon \n2)Crafting"))
        if choice == 1:
             selected_weapon = self.select_weapon()
             selected_weapon.expertise += 1 * hours
             print(f'{self.character.name} trained with {selected_weapon.name} for {hours} hours.\nNew weapon expertise: {selected_weapon.expertise}')
        elif choice == 2:
            self.character.craft+=(1*hours)
            print(f'{self.character.name} trained for {hours} hours.\n New craft expertise {self.character.craft}')
            
    def gather(self, hours):
        print(f"{self.character.name} looks for resources")
        self.character.search += hours
        if self.character.search + random.randint(0, 10) > 5:
            item = self.find_resource()
            quantity = self.find_quantity()
            self.character.equip_item(item, quantity)
            print(f"Found {quantity} units of {item}")
            self.tribe.update_cumulative_items()
            self.tribe.display_cumulative_items()
        else:
            print("Found nothing.")

    def find_resource(self):
        resources = ["Rocks", "Wood", "Meat"]
        return random.choice(resources)

    def find_quantity(self):
        return random.randint(1, 10)  
    
    def open_fight_menu(self, monster):
        while True:
            if monster.pf>0:
                print('What do you want to do?')
                choice = int(input('1) Fight\n2) Flight\n3) Tame \n'))
        
                if choice == 1:
                    # Call attack method
                    self.attack(monster)
                elif choice == 2:
                    # Call flight method
                    flight= self.flight()
                    if flight == True:
                        break
                elif choice == 3:
                    tame=self.tame(monster)
                    if tame == True:
                        break
            else: break
            
    def open_camp_menu(self):
        print('What do you want to do?')
        choice = int(input('1) Craft\n2) Rest\n3) Train \n4)Gather resources'))
        if choice == 1:
            self.craft()
        elif choice == 2:
            hours = int(input('How many hours do you want to rest?'))
            self.rest(hours)
        elif choice == 3:
            hours = int(input('How many hours do you want to train?'))
            self.train(hours)
        elif choice == 4:
            hours = int(input('How many hours do you want to do that?'))
            self.gather(hours)


 
        
 
'''    
 elif choice == 3:
            # Call craft method
            self.craft()
        elif choice == 4:
            # Call rest method
            self.rest()
'''
