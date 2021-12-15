import numpy as np
from queue import PriorityQueue
from dijkstra import get_path_cost

with open("input.txt") as fh:
	field = np.array([[int(c) for c in line.strip()] for line in fh], dtype=int)

start_pos = (0, 0)
goal_pos = (field.shape[0] - 1, field.shape[1] - 1)
path, cost = get_path_cost(start_pos, goal_pos, field)

print("Path length", len(path), "cost", cost)





