import numpy as np

with open("input.txt") as fh:
    crabs = np.array([int(c) for c in fh.read().strip().split(",")])

def f(x):
    return np.arange(x + 1).sum()

# one may observe (from the sample input) that the minimizing value is close to the mean,
# so lets use this heuristic to make calculations easier
m = int(np.mean(crabs).item())
fuel = [np.sum(np.vectorize(f)(np.abs(crabs - i))) for i in range(m - 5, m + 5)]
print(min(fuel))
