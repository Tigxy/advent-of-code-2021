from utils import *

with open("input.txt") as fh:
    nodes = [create_tree(parse(line)) for line in fh]

node = nodes[0]
for i in range(1, len(nodes)):
    node = add_nodes(node, nodes[i])
    while reduce(node):
        pass

magnitude = eval_magnitude(node)
print(magnitude)    # correct result: 3816
