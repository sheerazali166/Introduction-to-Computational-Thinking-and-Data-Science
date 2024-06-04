#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 08:11:30 2024

@author: sheeraz
"""

import random

print(random.randint(1, 5))

print(random.choice(['apple', 'cat', 'banana']))

def getEven():
    
    num = random.randint(0, 99)
    
    if num % 2 == 0:
        return True
    else:
        return False


print(getEven())

print("----------------")

""" 1. Are the following two distributions equivalent? """


def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1
    
print(dist1())
print(dist2())

print("----------------")

if dist1() == dist2():
    print("They are euqal")
else:
    print("They are not equal") 
    
    
""" 2. Are the following two distributions equivalent? """

import random

def dist3():
    return int(random.random() * 10)

def dist4():
    return random.randrange(0, 10)


print("----------------")


print(dist3())
print(dist4())

if dist3() == dist4():
    print("Dist3() and Dist4() are equal")
else:
    print("Dist3() and Dist4() are not equal")
    
    
""" 3. Are the following two distributions equivalent? """ 

def dist5():
    return int(random.random() * 10)

def dist6():
    return random.randint(0, 10)



print("----------------")


print(dist5())
print(dist6())

if dist5() == dist6():
    print("Dist5() and Dist6() are equal")
else:
    print("Dist5() and Dist6() are not equal")
    
    
    
    
    


    
    
    
    
    
    
    
    
    
    
    