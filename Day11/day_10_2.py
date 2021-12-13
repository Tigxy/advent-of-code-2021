import numpy as np

with open("input.txt") as fh:
	field = np.array([[int(c) for c in line.strip()] for line in fh])
print(field.shape)
print(field, "\n")

kernel = np.ones((3,3))
kernel[1,1] = 0

def broadcast(field, pos, lightened_poses):
	x, y = pos
	
	if field[x][y] > 9 and pos not in lightened_poses:
		field[x][y] = 0
		lightened_poses.append(pos)
		
		x_min, x_max = max(0, x - 1), min(field.shape[0], x + 2)
		y_min, y_max = max(0, y - 1), min(field.shape[1], y + 2)
		
		b = field[x_min : x_max,  y_min : y_max]
		
		field[x_min : x_max,  y_min : y_max] += 1
		a = np.argwhere(field >= 9)
		for x, y in a:
			broadcast(field, (x,y), lightened_poses)

first_step_simultaniously = None
n_steps = 300
sum_lightings = 0
for i in range(n_steps):
	# step
	field += 1

	# need to ensure that each position only lights once  per step
	lightened_poses = []
	a = np.argwhere(field > 9)
	
	for x,y in a:
		broadcast(field, (x,y), lightened_poses)
	for x,y in lightened_poses:
		field[x,y] = 0
	sum_lightings += len(lightened_poses)
	print(field, "\n")
	
	if len(lightened_poses) == field.shape[0] * field.shape[1]:
		print("first simultanious step at step", i + 1)
		break