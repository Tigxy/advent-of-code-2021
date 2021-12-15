import numpy as np
from queue import PriorityQueue
from dijkstra import get_path_cost

with open("input.txt") as fh:
	field = np.array([[int(c) for c in line.strip()] for line in fh], dtype=int)

n_times = 5
tile_size_x, tile_size_y = field.shape
nfield = np.zeros((tile_size_x * n_times, tile_size_y * n_times), dtype=int)

# Duplicate field
for i in range(n_times):
	for k in range(n_times):
		tile = field.copy() + (i+k)
		tile[tile > 9] -= 9
		nfield[tile_size_x * i : tile_size_x * (i + 1), tile_size_y * k : tile_size_y * (k + 1)] = tile

# Start up dijkstra
start_pos = (0, 0)
goal_pos = (nfield.shape[0] - 1, nfield.shape[1] - 1)
path, cost = get_path_cost(start_pos, goal_pos, nfield)

print("Path length", len(path), "cost", cost)





