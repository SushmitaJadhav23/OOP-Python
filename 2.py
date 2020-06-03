# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 03:09:38 2020

@author: sush1
"""


# class, method, attribute, object
class Hobbies:
    
    def __init__(self, name):
        self.name = name
    
h1 = Hobbies("Chicken Gravy")
h2 = Hobbies("Indian serials")
print(h1.name)
print(h2.name)

# differentiate difference between classes variable vs objects variable

class BestCourse:
    website = "http://cleverprogrammer.com"
    
    def __init__(self, name):
        self.name = name
        
        
course = BestCourse("Learn Python")
learn_command_line_course = BestCourse('learn command line')

print(course.name) #OBJECT_NAME.METHOD
print(learn_command_line_course.name)
print(BestCourse.website)  #CLASSNAME.METHOD

