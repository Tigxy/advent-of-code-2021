from queue import LifoQueue
import numpy as np

points = {')': 1, ']': 2, '}': 3, '>': 4}

openers = list("<{[(")
closers = list(">}])")
opener_closer = {o:c for o,c in zip(openers, closers)}

with open("input.txt") as fh:
	lines = [line.strip() for line in fh]
	
invalid_lines = []
for i, line in enumerate(lines):
	opened_chars = LifoQueue()
	for char in line:
		if char in openers:
			opened_chars.put(char)
		elif char in closers:
			if opened_chars.empty():
				invalid_lines.append((i, char))
				break
			
			chr = opened_chars.get()
			if char != opener_closer[chr]:
				invalid_lines.append((i, char))
				break
				
print(len(invalid_lines), "invalid lines")
for i, _ in invalid_lines[::-1]:
	del lines[i]
print(len(lines), "lines remaining")



scores = []
for i, line in enumerate(lines):
	opened_chars = LifoQueue()
	for char in line:
		if char in openers:
			opened_chars.put(char)
		elif char in closers:			
			chr = opened_chars.get()
			if char != opener_closer[chr]:
				assert "some error"
	
	score = 0
	while not opened_chars.empty():
		c = opened_chars.get()
		missing_c = opener_closer[c]
		score *= 5
		score += points[missing_c]
	scores.append(score)
	
print(scores)
print(np.median(scores))
	