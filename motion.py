# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:51:35 2024

@author: Francesco Brandoli
"""
from monsters import *
from characters import *
import random
from functools import partial

class Location:
    def __init__(self, description):
        self.description = description
        self.exits = {}

    def set_exits(self, exits):
        self.exits = exits

    def get_description(self):
        return self.description

    def get_exits(self):
        return self.exits
    
    def generate_random_location(self):
        room_types = ['dense forest', 'clearing with a pond', 'rocky path', 'overgrown trail']
        directions = ['North', 'South', 'West', 'East']
        self.description = f"You see: {random.choice(room_types)}. A path is leading {random.choice(directions)}."


class Commands:
    def __init__(self):
        self.rooms = self.create_location()
        self.current_room = self.rooms        
        self.inventory = []

    def create_location(self):
        # Create the initial room
        return Location("You are in a snowy forest. There is a path leading to the north.")
   
    def move(self, direction):
        print(f"Moving {direction}...\n")
        self.current_room.generate_random_location()          
        print(self.current_room.get_description())
        
    def random_event(self):
        #Add random items or weapons
        events = [partial(generate_random_monster), partial(generate_random_character)] 
        random_event = random.choice(events)
        return random_event()


