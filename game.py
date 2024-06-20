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
    name = input("What's your name? ")
    class_name = input("What is your chosen class?\n1) Warrior\n2) Hunter\n3) Shaman\n")
    
    if class_name == '1':
        character = Warrior(name)
    elif class_name == '2':
        character = Hunter(name)
    elif class_name == '3':
        character = Shaman(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        character = Warrior(name)
    
    print(f"Character created:\n{character}")
    #Initialize motion
    command = Commands()
    menu = Menu(character)
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
                chance = random.randint(1, 100)
                if chance > 70 :
                    event = command.random_event()
                    if type(event) in character_classes :  
                        data = load_data()
                        chatbot(event, data)
                    elif type(event) in monster_classes:
                        while True:
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
    
    
    
    
