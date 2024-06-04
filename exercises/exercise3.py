#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 09:03:33 2024

@author: sheeraz
"""

""" The output of random.randint(1, 10) after a specific seed is shown below. """

import random

random.seed(9001)

print(random.randint(1, 10))

print(random.randint(1, 10))

print(random.randint(1, 10))

print(random.randint(1, 10))

print(random.randint(1, 10))

print('-----------------')

"""
    We would like you to solve this problem using just the above output, without using
    the interpreter. (Note that the actual output you get when you run the above commands is
    actually going to be 1, 5, 5, 2, 10) What is printed in the following programs? Separate
    new lines with commas - so the above output would be 1, 3, 6, 6, 7.

    Note! Try it out! """
    
random.seed(9001)

for i in range(random.randint(1, 10)):
    print(random.randint(1, 10))
    
print('-----------------')

random.seed(9001)

d = random.randint(1, 10)

for i in range(random.randint(1, 10)):
    print(d)
    
print('-----------------')

random.seed(9001)

d = random.randint(1, 10)

for i in range(random.randint(1, 10)):
    if random.randint(1, 10) < 7:
        print(d)
    else:
        random.seed(9001)
        d = random.randint(1, 10)
        print(random.randint(1, 10))
    







    