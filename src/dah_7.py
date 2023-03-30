#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 06:23:32 2022

@author: eunjoob
"""


input_path = '../input/221207.txt'

with open(input_path, 'r') as f:
    input_ = f.read().splitlines()
    
# Day 7-1
# Find the sum of the total sizes of directories
# Only directoris with up to 100000 size
# 0-9 a-z : size fname
# may count multiple times (subdirs)

# setting up the directory structure
## dir_info = {dir or f_name: [parent, size, type], }


# functions
def set_cwd(command, cwd, dir_info):
    if command.startswith('$ cd'):      
        dest = command.split(' ')[-1]
        if dest == '/': 
            return 'Home'
        if dest == '..': 
            return dir_info[cwd][0]
        else: 
            return dest

cwd = 'Home'
dir_info = {'Home': [None, 0, 'dir']}

def update_dir_info(c, dir_info, cwd = 'Home'):
    if c.startswith('$ cd'): 
        print('setting cwd to', end = ' ')
        cwd = set_cwd(c, cwd, dir_info)
        print(f"{cwd}: {dir_info[cwd]}")
    if c.strip() == '$ ls': 
        print(f'{cwd} contains...')
    if c.startswith('dir'): 
        dir_name = c.split(' ')[-1]
        try: 
            dir_info[dir_name][0] = cwd
            dir_info[dir_name][2] = 'dir'
        except KeyError:
            dir_info[dir_name] = [cwd, 0, 'dir']
        print(f"    {dir_name} ({dir_info[dir_name]})")
    if c[0].isdigit(): 
        fsize, fname = c.split(' ')
        fsize = int(fsize)
        dir_info[fname] = [cwd, fsize, 'file']
        print(f"    {fname} ({dir_info[fname]})")
        dir_info[cwd][1] += fsize
        print(f"adding to {cwd}: {fsize} ({dir_info[cwd]})")
    return dir_info, cwd
        

def get_sizable_dir(dir_info, max_size = 100000, min_size = 0): 
    ls = []
    for k, v in dir_info.items():
        if v[2] == 'dir' and v[1] <= max_size and v[1] >= min_size:
            ls.append(k)
    return ls

def get_total_size(ls, dir_info):
    return sum([dir_info[x][1] for x in ls])

def final_run(input_, dir_info, cwd):
    for x in input_:
        dir_info, cwd = update_dir_info(x, dir_info, cwd)
    return (get_total_size(get_sizable_dir(dir_info), dir_info))

print (f"Day 7-1: Total dir size: {final_run(input_[:15], dir_info, cwd)}")


        
    