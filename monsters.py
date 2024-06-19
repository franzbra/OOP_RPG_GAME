# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 23:36:45 2024

@author: Francesco Brandoli
"""
import random

class Monster:
    def __init__(self, name, experience, attack, defense, pf):
        self.name = name
        self.experience = experience
        self.attack = attack
        self.defense = defense
        self.pf = pf

class Mammooth(Monster):
    def __init__(self):
        super().__init__('Mammooth',200, 20, 30, 100)
        print(f'You found a majestic {self.name}, eating snow')
        
class mini_Mammoth(Monster):
    def __init__(self):
        super().__init__('Mini Mammooth',50, 5, 7, 25)
        print(f'You found a friendly {self.name}, playing with trees')


class Megatherium(Monster):
    def __init__(self):
        super().__init__('Megatherium',150, 5, 20, 50)
        print(f'It\'s a {self.name}, a huge sloth!')


class Titanoboa(Monster):
    def __init__(self):
        super().__init__('Titanoboa',200, 30, 30, 100)
        print(f'It\'s a {self.name}, do you really nead an explanation!?')

        
class Arthropleura(Monster):
    def __init__(self):
        super().__init__('Arthropleura',100, 10, 10, 30)
        print(f'You\'ve found a {self.name}, you should probably google it')

class Dimetrodon(Monster):
    def __init__(self):
        super().__init__('Dimetrodon',150, 30, 30, 70)
        print(f'You\'ve found a {self.name}, one of the latest')

monster_classes = [Mammooth, mini_Mammoth, Megatherium, Titanoboa, Arthropleura, Dimetrodon]

def generate_random_monster():
    random_monster_class = random.choice(monster_classes)
    return random_monster_class()

