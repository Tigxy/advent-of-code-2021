from queue import LifoQueue

points = {')': 3, ']': 57, '}': 1197, '>': 25137}

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
				
print(invalid_lines)

sum = 0
for i, chr in invalid_lines:
	sum += points[chr]
print(sum)