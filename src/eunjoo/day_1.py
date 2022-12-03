#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input_path = '../input/221201.txt'

with open(input_path, 'r') as f:
    input_ = f.read().splitlines()

in_cc = ', '.join([x for x in input_])
tmp = in_cc.split(", , ")

total_cals_ls = [sum([int(x) for x in gr.split(', ')]) for gr in tmp]

print(f"Day 1-1: The most calories: {max(total_cals_ls)}")

total_cals_ls.sort(reverse = True)
print(f"Day 1-2: Sum of top 3 calories: {sum(total_cals_ls[0:3])}")

