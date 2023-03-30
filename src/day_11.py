#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 21:49:16 2022

@author: eunjoob

Day 11 stupid monkeys tossing my stuff
starting items = [worry level for each item]
operation = how worry lv changes when inspected
test = how to throw based on worry lv

post-operation before test
worry level /= 3 then rounded down to int

moneky inspects/throws all items each turn
round = all monkeys took turns

"""

# Day 11-1: 20 round
# 2 monkeys with the max total nubmer of items inspected
# monkey business = multiply the two together

import math
import copy 
import numpy as np

input_path = '../input/221211.txt' # test results: 10605

with open(input_path, 'r') as f:
    input_ = f.read().splitlines()
    
# cleaning up inputs
notes = [x.strip() for x in input_]
notes_d = {}

# making notes a dict
for l in notes: 
    if l == '': pass
    l_start = l.split(' ')[0]
    if l_start == 'Monkey': 
        k = int(l.strip(':').split(' ')[-1])
        notes_d[k] = {'toss_cnt': 0}
    elif l_start == 'Starting': 
        items = l.split(': ')[1]
        notes_d[k]['items'] = [int(x) for x in items.split(', ')]
    elif l_start == 'Operation:': 
        change = l.split(': ')[1]
        notes_d[k]['change'] = change
    elif l_start == 'Test:': 
        test = l.split(' ')[-1]
        notes_d[k]['div_by'] = int(test)
    elif l_start == 'If': 
        if l.split(' ')[1] == 'true:': 
            true_monkey = int(l.split(' ')[-1])
            notes_d[k]['true_monkey'] = true_monkey
        else: 
            false_monkey = int(l.split(' ')[-1])
            notes_d[k]['false_monkey'] = false_monkey


def operation(str_eq:str, val) :
    equation = str_eq.split(' = ')[1]
    if '+' in equation:
        add = equation.split(' + ')[1]
        if add == 'old': 
            y = val + val
        else:
            y = val + int(add) 
    elif '*' in equation: 
        mul = equation.split(' * ')[1]
        if mul == 'old': 
            y = val * val
        else: 
            y = val * int(mul)
    return y

def test(div_by, val): 
    return val % div_by == 0

def worry_less(val): 
    return int(math.floor(val/3))

def run_1(notes_d, rounds): 
    notes_d1 = copy.deepcopy(notes_d)
    for r in range(0, rounds): 
        for m in range(0, len(notes_d1)): 
            list_cnt = len(notes_d1[m]['items'])
            while list_cnt > 0:
                worry = notes_d1[m]['items'][0]
                # operation
                change = notes_d1[m]['change']
                new_worry = operation(change, worry)
                # worry level decreases
                new_worry = worry_less(new_worry)
                # test
                divby = notes_d1[m]['div_by']
                test_result = test(divby, new_worry)
                # throw
                notes_d1[m]['items'].pop(0)
                list_cnt -= 1
                if test_result: 
                    dest = notes_d1[m]['true_monkey']
                    notes_d1[dest]['items'].append(new_worry)
                    notes_d1[m]['toss_cnt'] += 1
                else:
                    dest = notes_d1[m]['false_monkey']
                    notes_d1[dest]['items'].append(new_worry)
                    notes_d1[m]['toss_cnt'] += 1
                    # print(f"....tossing to monkey {dest}")
                # print('')
    return notes_d1

day_1 = run_1(notes_d, 20)
a = [x['toss_cnt'] for x in day_1.values()]
a.sort(reverse = True)
print (f"Day 11-1: Monkey Business {a[0] * a[1]}.")
    

"""
Day 11-2
no more /3 worry less
10000 rounds

- new worry level affects the modulus during test
- operations only contain plus and multiplication
- so if we drop worry level to be its modulus
- divisor of product of all div by
- it should work?

"""

rounds = 10000

def run_2(notes_d, rounds): 
    notes_d2 = copy.deepcopy(notes_d)
    divisor_product = np.prod([x['div_by'] for x in notes_d2.values()])
    for r in range(0, rounds): 
        for m in range(0, len(notes_d2)): 
            list_cnt = len(notes_d2[m]['items'])
            while list_cnt > 0:
                worry = notes_d2[m]['items'][0]
                # operation
                change = notes_d2[m]['change']
                new_worry = operation(change, worry)
                # test
                divby = notes_d2[m]['div_by']
                if new_worry >= divisor_product: 
                    new_worry = new_worry%divisor_product
                test_result = test(divby, new_worry)
                # throw
                notes_d2[m]['items'].pop(0)
                list_cnt -= 1
                if test_result: 
                    dest = notes_d2[m]['true_monkey']
                    notes_d2[dest]['items'].append(new_worry)
                    notes_d2[m]['toss_cnt'] += 1
                else:
                    dest = notes_d2[m]['false_monkey']
                    notes_d2[dest]['items'].append(new_worry)
                    notes_d2[m]['toss_cnt'] += 1
    return notes_d2

day_2 = run_2(notes_d, 10000)
b = [x['toss_cnt'] for x in day_2.values()]
b.sort(reverse = True)
print (f"Day 11-2: Monkey Business {b[0] * b[1]}.")
    






