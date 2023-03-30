#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 17:29:49 2022

@author: eunjoob

Day 12-1: Hill Climbing Algo
input_ = heightmap
a:z = lowest : highest elevation
S = current position
E = best signal location
S has a elev
E has z elev
goal is to reach E in as few steps as possible
move one in 4 directions if elev diff is <= 1 (in letter)
get step counts
test output = 31 steps

"""

#0. parsing input
input_path = '../input/221212_test.txt' 

with open(input_path, 'r') as f:
    input_ = f.read().splitlines()

heightmap = [[*x] for x in input_]


def find_spot(hm, target:str): 
    '''
    '''
    for c_num in range(0, len(hm)): 
        for r_num in range(0, len(hm[c_num])): 
            if hm[c_num][r_num] == target:
                return [c_num, r_num]

def assign_node_id(m:list): 
    locations = []
    for c_num in range(0, len(m)): 
        for r_num in range(0, len(m[c_num])): 
            locations.append([c_num, r_num])
    return dict(zip(range(0, len(locations)), locations))


# get locations of of available nodes
def feasible_nodes(m, s): 
    ''' height map, S position'''
    m_size = [len(m), len(m[0])]
    c = s[0]
    r = s[1]
    nlist = [[c-1, r], [c+1, r], [c, r-1], [c, r+1]]
    newlist = []
    for n in nlist: 
        if 0 <= n[0] < m_size[0] and 0 <= n[1] < m_size[1]: # ones not edges
            th = m[n[0]][n[1]]
            ch = m[c][r]
            ch = 'a' if ch == 'S' else ch
            th = 'z' if th == 'E' else th
            if (ord(ch) + 1 >= ord(th)) and (ord(ch) - 1 <= ord(th)):
                newlist.append(n)
    return newlist

    

class edge: 
    def __init__(self, head, tail): 
        self.head = head
        self.tail = tail

class node: 
    def __init__(self, node_id):
        self.node_id = node_id
        self.offsprings = []
    
    def add_offspring(self, nid, tail): 
        e = edge(nid, tail)
        self.offsprings.append(e)
                    
# def find_steos()
    
# finding the starting/ending position
S_loc = find_spot(heightmap, 'S')
E_loc = find_spot(heightmap, 'E')

# assigning node_id for each location for convenience
node_map = assign_node_id(heightmap)

# building a directed graph


    
    
    
    
    
    
    
    
        