#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 09:41:43 2022

@author: eunjoob
"""

input_path = '../input/221204.txt'

with open(input_path, 'r') as f:
    input_ = f.read().splitlines()


# Day 4-1: Find the number of pairs where one fully contains the other
pairs = [[y.split('-') for y in x.split(',')] for x in input_]

def subgroup_test(p0, p1): 
    min_a = int(p0[0])
    min_b = int(p1[0])
    max_a = int(p0[1])
    max_b = int(p1[1])
        
    if min_a <= min_b: 
        if max_a >= max_b: 
            return True
    if min_b <= min_a: 
        if max_b >= max_a: 
            return True
    return False
            
total = sum([int(subgroup_test(p[0], p[1])) for p in pairs])
print (f"Day 4-1: Total Pairs CNT: {total}")



# Day 4-2: Get any overlaps

def overlaps(p0, p1): 
    return set(range(int(p0[0]), int(p0[1])+1)) & set(range(int(p1[0]), int(p1[1])+1))
    
total2 = sum([int(len(overlaps(p[0], p[1])) > 0) for p in pairs])
print (f"Day 4-2: All Overlapped Pairs CNT: {total2}")
