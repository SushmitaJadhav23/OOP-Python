# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 11:08:15 2020

@author: sush1
"""

# String representation , method, classes, objects
# Method: init

class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10
        
    #create method attack
    def attack(self, other_guy):
        other_guy.health = other_guy.health - self.damage
        print("{} attacks {}".format(self.name, other_guy.name))
        print("{} loses {} health points".format(other_guy.name, other_guy.damage))
    
    #over write print function for player 1
    def __str__(self):
        return "{}:{}".format(self.name, self.health)
        
        
player1 = Fighter('sushmita')
player2 = Fighter("Aakash")

print(player1) #print object player1
print(player2)
print(player1.name)
print(player2.name)

player2.attack(player1)
print(player1)
print(player2)
#now after attack sushmita has health of 90

