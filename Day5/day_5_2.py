import numpy as np

with open("input.txt") as fh:
	coordinates = [[[int(c) for c in s.strip().split(",")] for s in line.strip().split("->")] for line in fh]
	
coordinates_x = [a[0] for c in coordinates for a in c]
coordinates_y = [a[1] for c in coordinates for a in c]

field = np.zeros(shape=(max(coordinates_x) + 1, max(coordinates_y) + 1), dtype=np.int32)
print("Field size:", field.shape)

for c in coordinates:
	x1, y1, x2, y2 = [__c for _c in c for __c in _c]
	if x1 != x2 and y1 != y2:
		sign_x = 1 if x2 - x1 > 0 else -1
		sign_y = 1 if y2 - y1 > 0 else -1
		for i in range(0, abs(x2 - x1) + 1):
			field[x1 + i * sign_x, y1 + i * sign_y] += 1 
	else:
		x1, x2 = min(x1, x2), max(x1, x2)
		y1, y2 = min(y1, y2), max(y1, y2)
		field[x1:x2+1, y1:y2+1] += 1
	#print(f"{x1},{y1} -> {x2},{y2}")
	#print(c)
	#print(field.T)

print(field)

more_than_two = field > 1
print("Fields with more than two", more_than_two.sum())

