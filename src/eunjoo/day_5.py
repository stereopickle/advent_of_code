#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 08:19:18 2022

@author: eunjoob
"""
import copy

input_path = '../input/221205.txt'

with open(input_path, 'r') as f:
    input_ = f.read().splitlines()
    
    
    
# Day 5-1: Concatenated labels of top crates

instructions = input_[10:]
crates_raw = input_[:8]

tmp = [list(x) for x in crates_raw]


## setting up the crates

crates = []
for n in range(1, len(tmp[0]), 4): 
    crates.append([r[n] for r in tmp if r[n] != ' '])
        
    
## instruction logic

def move_crates(inst, cr):
    inst_s = inst.split()
    how_many = int(inst_s[1])
    from_ind = int(inst_s[3])-1
    to_ind = int(inst_s[5])-1
    
    for n in range(0, how_many):
        val = cr[from_ind][0]
        cr[from_ind].pop(0)
        cr[to_ind].insert(0, val)
    return cr


crates_output = copy.deepcopy(crates)

for inst in instructions: 
    move_crates(inst, crates_output)

def get_top(cr): 
    return ''.join([x[0] for x in cr])

print (f"Day 5-1: Top Crates: {get_top(crates_output)}")




## Day 5-2: Same but multiple crates at the same time

def move_crates_together(inst, cr):
    inst_s = inst.split()
    how_many = int(inst_s[1])
    from_ind = int(inst_s[3])-1
    to_ind = int(inst_s[5])-1

    vals = cr[from_ind][0: how_many]
    cr[from_ind] = cr[from_ind][how_many:]
    cr[to_ind] = vals + cr[to_ind]
    return cr

crates_output2 = copy.deepcopy(crates)

for inst in instructions: 
    move_crates_together(inst, crates_output2)
    
print (f"Day 5-1: Top Crates: {get_top(crates_output2)}")


