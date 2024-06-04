#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:40:02 2024

@author: sheeraz
"""

NUMBER = 3

def look_for_other_things(myList):
    """Looks at all pairs of elements"""
    for n in myList:
        for m in myList:
            if n - m == NUMBER or m - n == NUMBER:
                return True
    return False


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
myList2 = [1, 2, 0, 4, 5, 6, 7, 8, 9, 10]
myList3 = [3,]

print(look_for_other_things(myList))
print(look_for_other_things(myList2))
print(look_for_other_things(myList3))

        