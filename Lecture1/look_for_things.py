#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 09:20:33 2024

@author: sheeraz
"""

NUMBER = 3

def look_for_things(myList):
    """Look at the all elemments"""
    for n in myList:
        if n == NUMBER:
            return True
        else:
            return False
        
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
myList2 = [1, 2, 0, 4, 5, 6, 7, 8, 9, 10]
myList3 = [3,]

print(look_for_things(myList))
print(look_for_things(myList2))
print(look_for_things(myList3))
        
    