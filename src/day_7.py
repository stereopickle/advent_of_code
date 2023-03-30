#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 19:22:53 2022

@author: eunjoob
"""

input_path = '../input/221207.txt'

with open(input_path, 'r') as f:
    input_ = f.read().splitlines()
    

class directory:
    def __init__(self, name : str, parent_dir: object = None):
        self.name = name
        self.flist = {}
        self.dirlist = []
        self.parent_dir = parent_dir
    
    def __str__(self):
        return self.name
    
    def cwd(self):
        return self.name
    
    def parent(self) :
        # return parent directory
        print(self.parent_dir)
        return(self.parent_dir)

    def ls(self):
        # list of stuff
        list_ = []
        for obj in self.dirlist: 
            if obj.cwd() not in list_:
                list_.append(obj.cwd())
        list_ += list(self.flist.keys())
        print(list_)
        return list_
        
    def touch_dir (self, dir_name: str):
        # add the items
        self.dirlist.append(directory(dir_name, self))
        
    def touch_file (self, fname: str, size: int):
        # add a file size combo
        self.flist[fname] = int(size)
    
    def size(self):
        # return the total size
        fsize = sum(self.flist.values())
        for d in self.dirlist:
            fsize += d.size()
        return fsize
    
    def get_subdir(self, sub_dir_name: str): 
        i = 0
        while i < len(self.dirlist):
            if str(self.dirlist[i]) == sub_dir_name:
                subdir = self.dirlist[i]
                break
            else: 
                i += 1
        return self.dirlist[i]
            
def find_dir(name: str, dirlist): 
    while i < len(dirlist): 
        if str(dirlist[i]) == name: 
            dir_ = dirlist[i]
            break
        else: 
            i += 1
    return dir_
    

dir_list = []
        
def process_command(line, dir_list: list):
    if line.startswith('dir'):
        cwd.touch_dir(line.split(' ')[-1])
        return cwd
    if line[0].isdigit():
        fsize , fname = line.split(' ')
        cwd.touch_file(fname, fsize)
        return cwd
    if line.startswith('$ cd'): 
        dest = line.split(' ')[-1]
        if dest == '/':
            return find_dir('Home')
        if dest == '..':
            return find_dir(str(cwd.parent()))
        else:
            return find_dir(dest)


df = directory('Home')

test = ['dir fts', 'dir jad', '132 ef.sd', '$ cd fts', 
        'dir asd', '234 wed.df', '$ cd ..', '$ cd ..', 
        '123 cd.sa', 'dir 123']

dirs = [df]
for l in test[0:5]: 
    print(l)
    outp = process_command(l, dirs[0], dirs):
    if str(outp) in dirs: 
        