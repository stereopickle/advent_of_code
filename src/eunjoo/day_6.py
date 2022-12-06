#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 06:59:38 2022

@author: eunjoob
"""

input_path = '../input/221206.txt'

with open(input_path, 'r') as f:
    input_ = f.read().splitlines()[0]
    
# Day 6: find the first marker 
# Day 6-1: 4 consecutive different characters // index the last
# Day 6-2: 14 consecutive different characters // index the last


def find_fst_marker_ind(str_, n = 4):
    int_inp = [*str_]
    a_set = int_inp[0:n]
    i = n
    while i < len(int_inp):
        if len(set(a_set)) == n: 
            break
        else:
            a_set.pop(0)
            a_set.append(int_inp[i])
            i += 1
    return i, ''.join(a_set)

print (f"Day 6-1: Start-of-packet ind: {find_fst_marker_ind(input_)}")
print (f"Day 6-2: Start-of-message ind: {find_fst_marker_ind(input_, n = 14)}")


            
        
    
