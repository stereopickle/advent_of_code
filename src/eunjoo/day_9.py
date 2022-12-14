#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 15:04:10 2022

@author: eunjoob

Day 9 : Rope Bridge

input - series of motions
Tail and head are always touching
(diagonally, on the same line, overlapping)

1. If the head moves 2 steps 
tail move one step in the direction
2. If the head moves away 
when they are not already in the same line
tail follows diagonally 1 step

Day 9-1: Get the number of position 
that tail visited at least once
"""


# Logic
## Head movement type
# U = H_y + 1
# D = H_y - 1
# L = H_x - 1
# R = H_x + 1
## LOG Tail coordinates 

# calculating distance
# If H_x, H_y == T_x, T_y: dist = 0
# If x or y are the same,
#     but the other abs difference of other coord > 0
#     then dist = abs value
# If neither x or y are the same, 
#     dist = max(abs(x diff, y diff)) 
#     -> weird, but we won't get large diffs anyway

# After H moves, 
# If the dist is 0 or 1
#     T stays    
# If the dist > 1
#     whichever coord that is max(abs(diff)) gets - 1 for Tail
    
import copy

input_path = '../input/221209.txt'

with open(input_path, 'r') as f:
    input_ = f.read().splitlines()

def read_line(line): 
    direction, times = line.split(' ')
    return direction, int(times)

def get_dist(Hc, Tc): 
    if Hc == Tc: return 0 
    elif Hc[0] == Tc[0]: return abs(Hc[1] - Tc[1])
    elif Hc[1] == Tc[1]: return abs(Hc[0] - Tc[0])
    else: 
        return max(abs(Hc[0] - Tc[0]), abs(Hc[1] - Tc[1]))
    
def move_head(Hc, direction): 
    if direction == 'U': 
        return [Hc[0] - 1, Hc[1]] # reversed because starting low
    elif direction == 'D': 
        return [Hc[0] + 1, Hc[1]] # reversed because starting low
    elif direction == 'L':
        return [Hc[0], Hc[1] -1]
    elif direction == 'R':
        return [Hc[0], Hc[1] +1]
    else: print ('wtf')
    
def move_tail(Hc, Tc): 
    tmp_Tc = Tc[:]
    dist = get_dist(Hc, Tc)
    if dist < 2: 
        return Tc, dist
    else:
        if abs(Hc[0] - Tc[0]) > abs(Hc[1] - Tc[1]): # moving further vertically
            if Hc[0] > Tc[0]: # H sits below T
                tmp_Tc[0] += 1
                if Hc[1] > Tc[1]: # H sits right of T
                    tmp_Tc[1] += 1 # reversed because starting low
                elif Hc[1] < Tc[1]: # H sits left of T
                    tmp_Tc[1] -= 1
                else: 
                    pass
            else: # H sits above T
                tmp_Tc[0] -= 1
                if Hc[1] > Tc[1]: # H sits right of T
                    tmp_Tc[1] += 1 # reversed because starting low
                elif Hc[1] < Tc[1]: # H sits left of T
                    tmp_Tc[1] -= 1
                else: 
                    pass
        else: # moving further horizontally
            if Hc[1] > Tc[1]: # H sits right of T
                tmp_Tc[1] += 1
                if Hc[0] > Tc[0]: # H sits below T
                    tmp_Tc[0] += 1
                elif Hc[0] < Tc[0]: # H sits above T
                    tmp_Tc[0] -= 1
                else:
                    pass
            else: # H sits left of T
                tmp_Tc[1] -= 1
                if Hc[0] > Tc[0]: # H sits below T
                    tmp_Tc[0] += 1
                elif Hc[0] < Tc[0]: # H sits above T
                    tmp_Tc[0] -= 1
                else:
                    pass
        return tmp_Tc, dist


# stupid starting position is lower left do I care...?
Hc = [500, 500] # y, x
Tc = [500, 500] # y, x
i = 0
log = {0: {'line': None, 'Hc': Hc, 'Tc': Tc, 'dist': 0}}

for l in input_: 
    direction, times = read_line(l)
    for t in range(0, times): 
        i += 1
        Hc = move_head(Hc, direction)
        Tc, dist = move_tail(Hc, Tc)
        log[i] = {'line': l, 'Hc': Hc, 'Tc': Tc, 'dist': dist}
        
# get all the unique Tc locations 
cnt_tc = len(set([f"{v['Tc']}" for v in log.values()]))
print (f"Day 9-1: Tree position counts {cnt_tc}.")




# Day 9-2: 10th knot path

Hc = [500, 500] # y, x
Tc = [500, 500] # y, x
i = 0
log2 = {0: {'line': None, 'Hc': Hc, 'last_Tc': Tc}}
pos = dict.fromkeys(range(0, 10), Hc)

for l in input_:
    direction, times = read_line(l)
    #print(f"moving head to {direction}")
    for t in range(0, times):
        #print(f"    {t+1}.")
        i += 1
        Hc = move_head(pos[0], direction) # move the head
        pos[0] = Hc
        #print(f"    head is at {Hc}")
        for n in range(1, 10): 
            newTc = move_tail(pos[n-1], pos[n])[0]
            #print(f"    knot {n} following {pos[n-1]} moves from {pos[n]} to {newTc}")
            pos[n] = newTc
        #print(f"    tail is at {newTc}")

        log2[i] = {'line': l, 'Hc': Hc, 'last_Tc': newTc}

# get all the unique Tc locations 
cnt_tc2 = len(set([f"{v['last_Tc']}" for v in log2.values()]))
print (f"Day 9-2: Tree position counts {cnt_tc2}.")


