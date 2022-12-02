import pandas as pd
import numpy as np
import pytest

import data

FILE = "data/day_1.txt"


def read_data_with_nulls(data):
	with open(data) as f:
		df = pd.read_csv(f, header=None, skip_blank_lines=False, na_values=np.nan)
	
	return df


def read_data_to_df(data):
	with open(data, "r+") as f:
		df = pd.read_csv(f, header=None)
	
	return df


def day_1(data):
	elves_list = []
	curr_sum = 0
	with open(data, 'r') as f:
		elf_string = f.read().split('\n')
		
		for e in elf_string:
			
			if e != '':
				curr_sum += int(e)
			else:
				elves_list.append(curr_sum)
				curr_sum = 0
	
	#this is the answer to day 1
	print(max(elves_list))
	
	return elves_list
	
def day_1_b(data):
	sorted_elf_list = sorted(data, reverse=True)
	top_three = sorted_elf_list[:3]
	print(sum(top_three))
	return top_three
	

if __name__ == "__main__":
	# print(read_data_to_df(FILE))
	# print(read_data_with_nulls(FILE)[:10])
	df = read_data_with_nulls(FILE)
	elf_list = day_1(FILE)
	day_1_b(elf_list)
