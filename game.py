# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 22:10:22 2024

@author: Francesco Brandoli
"""
import random

from weapons import * 
from spells import *
from characters import *
from monsters import *
from menu import *
from motion import *


if __name__ == "__main__":
    name = input("What's your name? \n")
    class_name = input("What is your chosen class?\n1) Warrior\n2) Hunter\n3) Shaman\n")
    
    if class_name == '1':
        player = Warrior(name)
    elif class_name == '2':
        player = Hunter(name)
    elif class_name == '3':
        player = Shaman(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        player = Warrior(name)
    
    print(f"Character created:\n{player}")
    #Initialize classes
    command = Commands()
    tribe_name = input('Choose a name for your tribe \n')
    tribe = Tribe(tribe_name)
    tribe.add_character(player)
    menu = Menu(player, tribe)
    time = 0
    print("Welcome to the Adventure Game!")
    print(command.current_room.get_description())
    
    while True:
        text = input("> ").lower().split()
        if not text:
            continue
    
        verb = text[0]
        if verb == "go":
            if len(text) > 1:
                command.move(text[1])
                chance = random.randint(1, 100) + player.faith
                if chance > 70 :
                    event = command.random_event()
                    if type(event) in character_classes :  
                        data = load_data()
                        join = chatbot(player, event, data)
                        if join == True : 
                         tribe.add_character(event)
                         tribe.display_characters()
                         tribe.update_cumulative_items()
                         tribe.display_cumulative_items()

                    elif type(event) in monster_classes:
                            menu.open_fight_menu(event)
                else :
                    menu.open_camp_menu()
                
            else:
                print("Go where?")
                
        elif verb == "look":
            print(command.current_room.get_description())
        elif verb == "quit":
            print("Thanks for playing!")
            break
        else:
            print("I don't understand that command.")
        time=time_flows(time)
        time,night = day_to_night(time)
        if night == True:
            game= tribe.consume_food()
            if game == True:
                print('Your tribe is dead')
                print('Game over :(')
                break
    
 
    
    
