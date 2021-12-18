from .utils import *
from itertools import permutations


with open("input.txt") as fh:
    nodes = [line for line in fh]

magnitudes = [eval_magnitude(fully_reduce(add_nodes(first, second))) for first, second in permutations(nodes, 2)]
print(max(magnitudes))    # correct result: 4819
