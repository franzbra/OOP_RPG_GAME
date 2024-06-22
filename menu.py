# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 00:06:10 2024

@author: Francesco Brandoli
"""
import random
import sys
from tribe import *
from Prehistoric_functions import *
from items import *
from weapons import *

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

    def consume_stamina(self, hour):
        self.character.pf -= 1*hour
        print(f"You consumed {1*hour} pf. PF = {self.character.pf}")

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
               if item in ["Meat", "Bones"]:
                   self.character.equip_item(item, quantity)
                   print(f"{self.character.name} obtains {quantity} {item} from {monster.name}.") 
                   self.tribe.update_cumulative_items()
                   self.tribe.display_cumulative_items()
            return True
        else:
            print(f"{monster.name} has {monster.pf} PF remaining.")
            return False


    def monster_attack(self, monster):
        # Simulate an attack action
        print(f"{self.character.pf}")
        print(f"{monster.name} attacks!")
        dead = False
        if monster.attack > self.character.dexterity:
            monster_damage = monster.attack
            self.character.pf -= monster.attack
            print(f"{self.character.name} takes {monster_damage} damage! PF: {self.character.pf}")
        else : 
            print(f"{self.character.name} avoids the attack!")   
            return dead
        # Check if the character is defeated
        if self.character.pf <= 0:
            dead = True
            print(f"{self.character.name} was killed by a {monster.name}")
            return dead


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

    def craft(self,item_name):
        if item_name not in crafting_recipes:
            print(f"Recipe for {item_name} does not exist.")
            return
    
        recipe = crafting_recipes[item_name]
        required_level = recipe["crafting_level"]
        ingredients = recipe["ingredients"]
    
        if self.character.craft < required_level:
            print(f"{self.character.name} does not have the required crafting ability to craft {item_name}. Required level: {required_level}, Current level: {self.character.craft}.")
            return
    
        cumulative_items = self.tribe.cumulative_items
        
        # Check if all required items are available
        for ingredient, quantity in ingredients.items():
            if cumulative_items.get(ingredient, 0) < quantity:
                print(f"Not enough {ingredient} to craft {item_name}.")
                return
    
        # Deduct the required items from cumulative_items
        for ingredient, quantity in ingredients.items():
            cumulative_items[ingredient] -= quantity
        
        # If the item is a weapon, it's immediately equipped by the player.
        if item_name in weapons_classes:
            weapon_class = weapons_classes.get(item_name)
            weapon = weapon_class()
            print(weapon)
            self.character.equip_weapon(weapon)
            print(f"{item_name} has been crafted successfully by {self.character.name}.")
            self.tribe.display_cumulative_items()
            return
    
        # Add the crafted item to the tribe's cumulative items
        if item_name in cumulative_items:
            cumulative_items[item_name] += 1
        else:
            cumulative_items[item_name] = 1
        print(f"{item_name} has been crafted successfully by {self.character.name}.")
        self.tribe.display_cumulative_items()

    def pray(self, hours):
        if hours > turn : 
            print(f'Time exceed the duration of the turn')
        else: 
            self.character.faith+=self.character.level*hours
            print(f"{self.character.name} prayed for {hours} hours")
    
    
    def rest(self, hours):
        if hours > turn : 
            print(f'Time exceed the duration of the turn')
        else: 
            print(f"{self.character.name} rested for {hours} hours and gained {self.character.level*hours} pf")
            self.character.pf+=self.character.level*hours
            print(f"PF ={self.character.pf}")
        
    def train(self, hours):
        if hours > turn : 
            print(f'Time exceed the duration of the turn')
        else: 
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
        if hours > turn : 
            print(f'Time exceed the duration of the turn')
        else: 
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
                    monster_dead= self.attack(monster)
                    if monster_dead == True:
                        break
                    character_dead = self.monster_attack(monster)
                    if character_dead == True :
                        print('Game over')
                        sys.exit()                   
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
        while True:
            print('What do you want to do?')
            choice = int(input('1) Craft\n2) Rest\n3) Train \n4) Gather resources \n5) Pray \n6)Statistics \n7)Nothing'))
            if choice == 1:
                self.character.list_recipes()
                item = input('What do you want to craft?')
                self.craft(item)
            elif choice == 2:
                hours = int(input('How many hours do you want to rest?\n'))
                self.rest(hours)
            elif choice == 3:
                hours = int(input('How many hours do you want to train?\n'))
                self.train(hours)
                self.consume_stamina(hours)
            elif choice == 4:
                hours = int(input('How many hours do you want to do that?\n'))
                self.gather(hours)
                self.consume_stamina(hours)
            elif choice == 5:
                hours = int(input('How many hours do you want to pray?\n'))
                self.pray(hours)
            elif choice == 6:
                choice = int(input('What do you want to see?\n1)See items you can craft \n2)See tribe items \n3)See tribe members\n'))
                if choice ==1:
                    self.character.list_recipes()
                elif choice ==2:
                    self.tribe.display_cumulative_items()
                elif choice ==3:
                    self.tribe.display_characters()
            elif choice == 7:
                break



 
        