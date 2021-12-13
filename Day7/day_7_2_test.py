import numpy as np

with open("input.txt") as fh:
    crabs = np.array([int(c) for c in fh.read().strip().split(",")])

def f(x):
    return int(x * (x+1) / 2)

fuel = [np.sum(np.vectorize(f)(np.abs(crabs - i))) for i in range(max(crabs))]
print(min(fuel))


import matplotlib.pyplot as plt
plt.plot(range(max(crabs)), fuel)
plt.show()