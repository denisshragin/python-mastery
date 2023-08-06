# art.py

import sys
import random

chars = '\|/'

def draw(rows, columns):
	for r in range(rows):
		# This four lines was added to explain myself the idea about usage of generators in the next PRINT statement
		# string = []
		# for _ in range(columns):
		# 	string.append(random.choice(chars))
		# print(''.join(string))
		print(''.join(random.choice(chars) for _ in range(columns)))

if __name__ == '__main__':
	if len(sys.argv) !=3:
		raise SystemExit("Usage: art.py row columns")
	draw(int(sys.argv[1]), int(sys.argv[2]))