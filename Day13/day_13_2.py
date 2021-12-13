import re
import numpy as np

positions = []
foldings = []

fold_regex = r"(\w)=(\d+)"

# Parse input file
sep_found = False
with open("input.txt") as fh:
	for line in fh:
		line = line.strip()
		if sep_found:
			g = re.search(fold_regex, line)
			foldings.append((g[1], int(g[2])))
		elif line == "":
			sep_found = True
		else:
			positions.append([int(c) for c in line.strip().split(",")])
			
max_x = max(x for x, _ in positions)
max_y = max(y for _, y in positions)

# Generate field
field = np.zeros((max_x + 1, max_y + 1), dtype=int) # +1  as field starts at (0,0)

for x, y in positions:
	field[x][y] = 1
	
print(field)

# Execute folding
for axis, coordinate in foldings:
	print(axis, coordinate)
	if axis == "x":
		part = field[:coordinate, :].copy()
		flipped_part = field[coordinate + 1:, :].copy() # ignore flipped line
		flipped_part = np.flipud(flipped_part)
		
		field = part
		field[field.shape[0] - flipped_part.shape[0]:, :] += flipped_part
		print(field)
		
	if axis == "y":
		part = field[:, :coordinate].copy()
		flipped_part = field[:, coordinate + 1:].copy()
		flipped_part = np.fliplr(flipped_part)
		print(part.shape, flipped_part.shape)
		
		field = part
		field[:, field.shape[1] - flipped_part.shape[1]:] += flipped_part
		print(field)
		
print("done, final field size:", field.shape)

# Code is 8 digits, so we split the field into 8 parts
part_size = int(field.shape[0] / 8)
print(part_size)
for i in range(8):
	part = field[i*part_size:i*part_size+part_size, :].copy()
	part[part > 1] = 1
	
	print()
	# Nicely print each of the field parts. We flip to have the X axis horizontal...
	for line in part.T.tolist():
		print("".join(["#" if c > 0 else "." for c in line]))
		
print()
print("Read the characters and enter them on the website!")