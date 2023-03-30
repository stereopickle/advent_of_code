#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:19:28 2022
@author: eunjoob
"""

## Day 2-1
# A B C : X Y Z : Rock Paper Scissor : 1 2 3

input_path = '../input/221202_1.txt'

with open(input_path, 'r') as f:
    input_ = f.read().splitlines()

score_map = {'C Y': 2, 'B X': 1, 'A Z': 3, 
             'C Z': 6, 'B Y': 5, 'A X': 4, 
             'C X': 7, 'B Z': 9, 'A Y': 8}
total = 0
for p in input_: 
    sc = score_map[p]
    total += sc    

print (f"Day 2-1: Total Score: {total}")


## Day 2-2
# A B C : Rock Paper Scissor : 1 2 3 
# X Y Z : W D L : 0 3 6

hands = [x.split(' ') for x in input_]

# outcome score
outcome_map = {'X': 0, 'Y': 3, 'Z': 6}
outcomes = [outcome_map[x[1]] for x in hands]

# hand score
# {'op_hand': [w, d, l]}
guide = {'A': [2, 1, 3], 'B': [3, 2, 1], 'C': [1, 3, 2]}

total_2 = 0
for x in input_: 
    hands = x.split(' ')
    op_hand = hands[0]
    if hands[1] == 'X': 
        total_2 += guide[op_hand][2]
    elif hands[1] == 'Y':
        total_2 += guide[op_hand][1]
    elif hands[1] == 'Z':
        total_2 += guide[op_hand][0]
    else:
        "something's wrong"

print (f"Day 2-2: Total Score (2): {sum(outcomes)+total_2}")

