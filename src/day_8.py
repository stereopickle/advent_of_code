#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 12:23:19 2022

@author: eunjoob
"""

import numpy as np


input_path = '../input/221208.txt'

with open(input_path, 'r') as f:
    input_ = f.read().splitlines()
    

# Day 8: trees
# get a matrix
i_max = np.array([int(x) for x in input_[0]])

for i in input_[1:]: 
    i_max = np.vstack([i_max, [int(x) for x in i]])
    
i_max = np.matrix(i_max)

def get_trees(y_i, x_i, tree_matrix): 
    if y_i == 0: 
        u_tr = []
    else: 
        u_tr = np.ravel(np.flip(tree_matrix[:y_i, x_i]))
        
    if y_i == tree_matrix.shape[0]-1:
        d_tr = []
    else:
        d_tr = np.ravel(tree_matrix[y_i+1:, x_i])
        
    if x_i == 0: 
        l_tr = []
    else:
        l_tr = np.ravel(np.flip(tree_matrix[y_i, :x_i]))
        
    if x_i == tree_matrix.shape[1]-1:
        r_tr = []
    else: 
        r_tr = np.ravel(tree_matrix[y_i, x_i+1:])
        
    return u_tr, d_tr, l_tr, r_tr

# Day 8-1: find all visible trees
# for each tree, check visibility
def is_visible(y_i, x_i, tree_matrix): 
    # A tree is visible if all of the other trees between it 
    # and an edge of the grid are shorter than it. 

    tree_hgt = tree_matrix[y_i, x_i]
    u_tr, d_tr, l_tr, r_tr = get_trees(y_i, x_i, tree_matrix)
    if max(u_tr, default = -1) < tree_hgt \
        or max(d_tr, default = -1) < tree_hgt \
        or max(l_tr, default = -1) < tree_hgt\
        or max(r_tr, default = -1) < tree_hgt: 
        return True
    else: 
        return False

y_max, x_max = i_max.shape
visible_trees = 0

for y_i in range(0, y_max): 
    for x_i in range(0, x_max):
        if is_visible(y_i, x_i, i_max): 
            visible_trees += 1

# Day 8-2: find the highest scenic score
# scenic score = product of trees visible from all 4 sides
 
    
def scenic_score(y_i, x_i, tree_matrix): 
    tree_hgt = tree_matrix[y_i, x_i]
    u_tr, d_tr, l_tr, r_tr = get_trees(y_i, x_i, tree_matrix)
    score = []
    #get the first blocker tree index 
    # UP
    for tr_ls in (u_tr, d_tr, l_tr, r_tr): 
        if tr_ls == []: 
            pass
        elif max(tr_ls) < tree_hgt: 
            score.append(len(tr_ls))
        else:
            score.append(min([i for i, x in enumerate(tr_ls) if x >= tree_hgt]) + 1)
    return score


highest_score = 0 
high_com = [-1, -1, -1]
for y_i in range(0, y_max):
    for x_i in range(0, x_max): 
        if (sc:= np.prod(scenic_score(y_i, x_i, i_max))) > highest_score: 
            highest_score = sc
            
            
print (f"Day 8-1: Total visible trees {visible_trees}.")
print (f"Day 8-2: Highest scenic score {highest_score}")

