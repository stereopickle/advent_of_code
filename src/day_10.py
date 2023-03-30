#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 20:34:38 2022

@author: eunjoob

CPU has a single register X, starts with 1
1. addx V takes 2 cycles to complete.
After that X register is increased by V (can be negative)
2. noop takes one cycle to complete.

signal strength = cycle number x value of X
during 20th and every 40th after
"""

import numpy as np
input_path = '../input/221210.txt'

with open(input_path, 'r') as f:
    input_ = f.read().splitlines()

def process_line(l): 
    if l.strip() == 'noop': 
        val = 0
        add_cycles = 1
    else:
        val = l.split(' ')[-1]
        add_cycles = 2
    return int(val), add_cycles

x = 1
x_cld_vs = {0: x} # {cycle: value}
c = 0
for l in input_: 
    val, add_cycles = process_line(l)
    for n in range(0, add_cycles): 
        c += 1 # add cycle
        if n == 0: 
            x_cld_vs[c] = x_cld_vs[c-1]
        else: 
            x_cld_vs[c] = x_cld_vs[c-1] + val
    
    
# Day 10-1: sum of 6 (20th, 60th, 100th, 140th, 180th, and 220th) signal strength

cycles = [20, 60, 100, 140, 180, 220]
cyc_ind = [x-1 for x in cycles]
sel_vals = [x_cld_vs[i] for i in cyc_ind]

ss = np.array(cycles) * np.array(sel_vals)
print (f"Day 10-1: signal strength {sum(ss)}.")



"""
Day 10-2: 
    sprite = 3 px wide
    X sets the middle
    CRT: 40w x 6h moves L>R U>D (0 index)
    1 px per cycle
    if one of its 3 px is currently being drawn
    px = # otherwise .
    (basically if +/- from X overlaps with where
     CRT is now, it'll draw # otherwise .')
    
"""

# x_cld_vs represents the middle of sprite each cycle
# if the value +/- 1 = the cycle number, #, if not 0
# but for 40 cycles, -40 from cycle (print separately)

for k, v in x_cld_vs.items():
    ind = k % 40 
    if ind == 0: # new line
        ending = '\n'
    else: 
        ending = ''
    if ind in (v-1, v, v+1): 
        print ('#', end=ending)
    else:
        print('.', end= ending)






