# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 02:36:35 2020

@author: sush1
"""


class Student:
    
    def __init__(self, name, grade,age):
        self.name = name
        self.grade = grade
        self.age = age
        

kitty = Student('Kitty', 85, 21)
daniel = Student('daniel', 80, 28)

print(kitty.name)
print(daniel.name)

print(daniel.grade)
print(daniel.age)