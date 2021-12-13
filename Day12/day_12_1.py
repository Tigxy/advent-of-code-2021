from queue import Queue
from collections import Counter

with open("input2.txt") as fh:
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

# more or less DFS
def search(cave, path_until_now, discovered_paths):
	cave_obj = cave_dict[cave]
	if cave in path_until_now and not cave_obj.is_large:
		return

	path = path_until_now + [cave]
	if cave == "end":
		discovered_paths.append(path)
		return
	
	for adj in cave_obj.adjacent:
		search(adj, path, discovered_paths)

discovered_paths = []
search("start", [], discovered_paths)
print(len(discovered_paths))