#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 08:41:45 2024

@author: sheeraz
"""

""" 1. Is the following code deterministic or stochastic? """

import random

myList = []

for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        myList.append(number)
        
print(myList)

""" 2. Which of the following alterations (Code Sample A or Code Sample B)
    would result in a deterministic process? """

print('-----------------------')

""" Code Sample A """

myList = []

for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        if number not in myList:
            myList.append(number)
            
print(myList)


""" Code Sample B """

myList = []

random.seed(0)
for i in range(random.randint(1, 10)):
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        myList.append(number)
    print(myList)    







            
            
        
    
    