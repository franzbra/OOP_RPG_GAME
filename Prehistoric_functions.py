# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 15:51:10 2024

@author: Francesco Brandoli
"""
import random
import json
from characters import *

# Components for generating names
prefixes = ["Kar", "Tor", "Nar", "Gor", "Zar", "Bar", "Lar", "Mor", "Rag", "Vor"]
suffixes = ["ak", "ik", "ar", "or", "ur", "an", "en", "un", "al", "il"]
endings = ["", "the Strong", "the Brave", "the Hunter", "the Wise", "the Swift", "of the Mountain", "of the River", "the Elder", "the Young"]

# Function to generate a single name
def generate_name():
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)
    ending = random.choice(endings)
    name = prefix + suffix
    if ending:
        name += " " + ending
    return name

def load_data():
    with open('character_data.json', 'r') as file:
        data = json.load(file)
    return data


def chatbot(character, data):
    if not character:
        print("No character was generated. Exiting chatbot.")
        return

    print(data["responses"]["greet"])
    
    while True:
        user_input = input("You: ").strip().lower()
        if user_input in ["quit", "exit", "bye"]:
            print(data["responses"]["farewell"])
            break
        elif "name" in user_input:
            print(f"{character.name}: My name is {character.name}.")
        elif "level" in user_input:
            print(f"{character.name}: I am at level {character.level}.")
        elif "experience" in user_input:
            print(f"{character.name}: I have {character.experience} experience points.")
        elif "attack" in user_input:
            print(f"{character.name}: My attack stat is {character.attack}.")
        elif "defense" in user_input:
            print(f"{character.name}: My defense stat is {character.defense}.")
        elif "pf" in user_input:
            print(f"{character.name}: My PF stat is {character.pf}.")
        elif "weapon" in user_input:
            weapon_name = str(character.weapon)
            print(f"{character.name}: I am equipped with a {type(weapon_name)}. {data['weapons'].get(weapon_name, '')}")
        elif "item" in user_input:
            item_name = str(character.item) if character.item else "nothing"
            print(f"{character.name}: I am carrying {item_name}. {data['items'].get(item_name, '')}")
        elif "title" in user_input:
            if character.title:
                titles = ", ".join(character.title)
                titles_info = ", ".join([data['titles'].get(title, '') for title in character.title])
                print(f"{character.name}: I have the following titles: {titles}. {titles_info}")
            else:
                print(f"{character.name}: I have no titles yet.")
        elif "magic" in user_input and isinstance(character, Shaman):
            print(f"{character.name}: I can cast {character.magic}.")
        else:
            print(data["responses"]["default"])
    