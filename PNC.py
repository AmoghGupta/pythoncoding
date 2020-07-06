#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 20:40:24 2020

@author: agupta
"""


from itertools import permutations 
  
# Get all permutations of length 2 
# and length 2 
perm = permutations([6,2,5,4,5,1,6], 2) 
max= 0

for a,b in perm:
    if a+b>max:
        max=a+b
print(max)