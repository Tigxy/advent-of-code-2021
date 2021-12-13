import numpy as np

with open("input.txt") as fh:
	field = [[int(c) for c in list(line.strip())] for line in fh]
field = np.array(field)
padded = np.full(fill_value=10, shape=(field.shape[0] + 2, field.shape[1] + 2))
padded[1:-1, 1:-1] = field
field = padded

kernel = np.array([[False,True,False], [True,False,True], [False,True,False]])

low_points = []
for x in range(1, field.shape[0] - 1):
	for y in range(1, field.shape[1] - 1):
		value = field[x, y]
		kvalue = field[x-1:x+2, y-1:y+2][kernel]
		
		if value < kvalue.min():
			low_points.append(value)
			
print(low_points)
print(sum(low_points) + len(low_points))
