#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:04:50 2022

@author: eunjoob
"""

# Day 3-1: Find the sum of priorities of common items across two compartments
## first half and second half indicates the 2 compartments 

input_path = '../input/221203_1.txt'

with open(input_path, 'r') as f:
    input_ = f.read().splitlines()

runsacks = [[x[:int(len(x)/2)], x[int(len(x)/2):]] for x in input_]

## common items
cm_items = [list(set(x[0]) & set(x[1]))[0] for x in runsacks]

## priorities
## priority (a z : 1 26, A Z : 27 52)

def get_priority(chr_): 
    if chr_.islower():
        return ord(chr_) - 96
    else: 
        return ord(chr_) - 38
    
total = sum([get_priority(x) for x in cm_items])    


print ("Day 3-1: Total Priorities", end = ": ")
print(total)



# Day 3-2: Find the sum of priorities of the badges (common across 3 consecutive runsacks)

total2 = 0

for i in range(0, len(input_), 3):
    badge = list(set(input_[i]) & set(input_[i+1]) & set(input_[i+2]))[0]
    total2 += get_priority(badge)

print ("Day 3-2: Total Priorities", end = ": ")
print(total2)
