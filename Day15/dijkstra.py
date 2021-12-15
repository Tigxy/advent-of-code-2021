import numpy as np
from queue import PriorityQueue

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# for backtracking, we have to reverse the directions
fdirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def apply_dir(pos, dir):
	return tuple([p+d for p, d in zip(pos, dir)])
		
def get_adj_and_cost(pos, field):
	x, y = pos
	
	adj_positions = [(dindex, field[npos], npos) for dindex, dir in enumerate(dirs) \
		if min(npos := apply_dir(pos, dir)) >= 0 \
		and all([p < s for p, s in zip(npos, field.shape)])]
	
	return adj_positions

def get_path_cost(start, goal, field):
	cost_field = np.zeros_like(field, dtype=int) # costs
	prev_dirs = np.zeros_like(field, dtype=int) # how we got there

	queue = PriorityQueue()
	queue.put((0, start))

	# determine cost to reach each position
	# Note: we cannot easily terminate beforehand, as its still possible that goal 
	# is reachable with lower cost (only with heuristic: manhatten distance and cost of next items in queue)
	while not queue.empty():
		cost, pos = queue.get()
		
		for dindex, c, p in get_adj_and_cost(pos, field):
			ncost = cost + c
			if ncost < cost_field[p] or cost_field[p] == 0:
				cost_field[p] = ncost
				prev_dirs[p] = dindex
				queue.put((ncost, p))

	# perform backtracking
	path = []
	current_pos = goal
	while True:
		dindex = prev_dirs[current_pos]
		current_pos = apply_dir(current_pos, fdirs[dindex])
		path.append(current_pos)
		if current_pos == start:
			break
			
	return path, cost_field[goal]