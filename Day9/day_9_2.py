import numpy as np
from collections import Counter

with open("input.txt") as fh:
	field = [[int(c) for c in list(line.strip())] for line in fh]
field = np.array(field)
padded = np.full(fill_value=10, shape=(field.shape[0] + 2, field.shape[1] + 2))
padded[1:-1, 1:-1] = field
field = padded

basins = np.zeros_like(field)
kernel = np.array([[False,True,False], [True,False,True], [False,True,False]])
dir_kernel = np.array([[0,1,0], [2,0,3], [0,4,0]])

dirs = [(0, -1), (-1, 0), (1, 0), (0, 1)]


basin_pos = []

# find basins and flow
for x in range(1, field.shape[0] - 1):
	for y in range(1, field.shape[1] - 1):
		value = field[x, y]
		kvalue = field[x-1:x+2, y-1:y+2][kernel]
		
		# dir with min value
		dv = np.argmin(kvalue).squeeze()
		dir = dirs[dv]
				
		if value <= kvalue.min():
			basins[x-1:x+2, y-1:y+2][kernel] = [1,2,3,4]
			basins[x, y] = 5
			basin_pos.append((x,y))
		else:
			basins[x, y] = dv+1
			
basins[field == 9] = 0
basins[field == 10] = 0
field[field == 10] = 0


def apply_dir(x, y, dir):
	return x+dir[0], y+dir[1]

basin_assignment = np.zeros_like(basins)
def assign_adjacent_positions(x, y, bv):		
	for v,d in [([1,4], (1,0)), ([1,4], (-1, 0)), ([2,3], (0,1)), ([2,3], (0, -1))]:
		pos = apply_dir(x,y,d)
		if basins[pos] in v:
			if basin_assignment[pos] == 0:
				basin_assignment[pos] = bv				
				assign_adjacent_positions(*pos, bv)

# recursively search for every basin the adjacent fields which flow to the basin
bcounter = 1
for p in basin_pos:
	basin_assignment[p] = bcounter 
	assign_adjacent_positions(*p, bcounter)
	bcounter += 1

# extract only actual field
basins = basins[1:-1, 1:-1]
basin_assignment = basin_assignment[1:-1, 1:-1]
			
for line in field:
	print("".join([str(c) if c > 0 else "." for c in line]))

for line in basins:
	print("".join([str(c) if c > 0 else "." for c in line]))
	
print()
	
a = [i for line in basin_assignment for i in line]
sorted_counter = sorted(Counter(a).items(), key=lambda x: x[1],reverse=True)	

values = [v for k,v in sorted_counter if k != 0][:3]	# take first three and ignore counts of 0
print("Result:", values[0] * values[1] * values[2])


