#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 09:32:47 2024

@author: sheeraz
"""

import random

""" 1. Option A) """

directionList = [(0.0, 1.0), (1.0, 0.0), (-1.0, 0.0), (0.0, -1.0)]

def optionA(myDirection):

    myDirection = random.choice(directionList)
    
    if myDirection[0] == 0.0:
        return myDirection + (0.0, -0.5)
    return myDirection


print(optionA(directionList))


print('----------------------')

""" Option B) """

directionList2 = [(0.0, 0.5), (1.0, -0.5), (-1.0, -0.5), (0.0, -1.5)]

def optionB(myDirection):
    return random.choice(myDirection)

print(directionList2)

print('-----------------------')

""" Option C) """

directionList3 = [(0.0, 0.5), (1.0, 0.0), (-1.0, 0.5), (0.0, -1.5)]

def optionC(myDirection):
    return random.choice(directionList)


print(optionC(directionList3))

print('-----------------------')

""" Option D) """

directionList4  = [(0.0, 1.0), (1.0, 0.0), (-1.0, 1.0), (0.0, -1.0), (0.0, -1.0)]

def optionD(myDirection):
    return random.choice(myDirection)

print(optionD(directionList4))





    