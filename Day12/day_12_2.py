from queue import Queue
from collections import Counter

with open("input.txt") as fh:
	paths = [line.strip().split("-") for line in fh]
caves = list({c for p in paths for c in p})

def is_large_cave(cave):
	return cave.upper() == cave
	
class cave:
	def __init__(self, name, adjacent): 
		self.name = name
		self.adjacent = adjacent
		self.is_large = is_large_cave(name)
		
cave_dict = {}
for c in caves:
	cave_dict[c] = cave(c, [pe if c == ps else ps for ps, pe in paths if c in [ps, pe]])

def count_small_caves(path):
	return Counter((c for c in path if not cave_dict[c].is_large))

# more or less DFS
def search(cave, path_until_now, discovered_paths):
	cave_obj = cave_dict[cave]
	path = path_until_now + [cave]
	
	if not cave_obj.is_large:
		cave_visits = count_small_caves(path)
		n_visits_twice = sum((1 if v >= 2 else 0 for v in cave_visits.values()))
		
		if cave_visits[cave] > 2 or n_visits_twice > 1:
			return

	if cave == "end":
		discovered_paths.append(path)
		return
	
	for adj in cave_obj.adjacent:
		if adj == "start":
			continue
		search(adj, path, discovered_paths)

discovered_paths = []
search("start", [], discovered_paths)
print(len(discovered_paths))