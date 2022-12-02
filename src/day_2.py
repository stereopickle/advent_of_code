import pandas as pd
import numpy as np
import pytest
import main
import data

FILE = "../data/day_2.txt"


def build_df(df):
	game_df = pd.DataFrame()
	final_df = pd.DataFrame()
	game_df = df.iloc[:,0].apply(lambda x: x.replace("A", '1'))\
		.apply(lambda x: x.replace("B", '2'))\
		.apply(lambda x: x.replace("C", '3'))\
		.apply(lambda x: x.replace("X", '1'))\
		.apply(lambda x: x.replace("Y", '2'))\
		.apply(lambda x: x.replace("Z", '3'))
	#game_df[['Elf', 'Me']] = df.iloc[:, 0].apply(lambda x: pd.Series(str(x).split()))
	
	final_df[['Elf', 'Me']] = game_df.apply(lambda x: pd.Series(str(x).split()))
	final_df['Elf'].astype(int)
	final_df['Me'].astype(int)
	final_df[['Elf_Threw', 'I_Throw']] = df.iloc[:,0].apply(lambda x: pd.Series(str(x).split()))
	final_df['Elf_Threw'].replace({'A': 'rock', 'B': 'paper', 'C':'scissors'}, regex=True, inplace=True)
	#final_df['I_Throw'].replace({'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}, regex=True, inplace=True)
	#updating for day 2 lose,draw,win
	final_df['I_Throw'].replace({'X': 'lose', 'Y': 'draw', 'Z': 'win'}, regex=True, inplace=True)
	
	
	final_df.rename_axis('idx', inplace=True)
	
	final_df['score'] = final_df.apply(lambda row: score(str(row['Elf_Threw']), row['I_Throw']), axis=1)
	final_df['score'].astype(int)
	final_df['total_score'] = final_df.apply(lambda row: np.add(int(row['score']), int(row['Me'])), axis=1)
	final_df['total_score'] = final_df.apply(lambda row: queued_score(row['Elf_Threw'], row['I_Throw']), axis=1)
	print(final_df)
	#print(final_df['total_score'] == 1)
	#print(np.sum(final_df['total_score']))
	return final_df
	
	
def score(elf, me):
	#print(elf, me)
	if str(elf) == 'scissors' and (str(me)!='scissors'):
		if me == 'paper':
			return 0
		else:
			return 6
	
	elif str(elf) == 'rock' and str(me) != 'rock':
		if me == 'scissors':
			return 0
		else:
			return 6
		
	elif str(elf) == 'paper' and str(me) != 'paper':
		if me == 'rock':
			return 0
		else:
			return 6
		
	else:
		return 3
	

def queued_score(elf: str, me: str) -> int:
	ROCK = 1
	PAPER = 2
	SCISSORS = 3
	
	if str(me) == 'draw':
		if str(elf) == 'scissors':
			return 3+3
		elif str(elf) == 'paper':
			return 2 + 3
		else:
			return 1 + 3
		
	elif str(elf) == 'scissors':
		if me == 'lose':
			return 2 + 0
		elif me == 'win':
			return 1 + 6
	
	elif str(elf) == 'rock':
		if me == 'lose':
			return 3 + 0
		elif me == 'win':
			return 2 + 6
	
	elif str(elf) == 'paper':
		if me == 'lose':
			return ROCK + 0
		elif me == 'win':
			return SCISSORS + 6

	


if __name__ == "__main__":
	# print(read_data_to_df(FILE))
	# print(read_data_with_nulls(FILE)[:10])
	df = main.read_data_to_df(FILE)
	day_2_df = build_df(df)
	solution = np.sum(day_2_df['total_score'])
	print(solution)

	
