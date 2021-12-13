import numpy as np

with open("input.txt") as fh:
    crabs = np.array([int(c) for c in fh.read().strip().split(",")])
    
fuel = [np.abs(crabs - i).sum() for i in range(max(crabs))]
print(min(fuel))
print(np.argmin(fuel))
print(np.median(crabs))

import matplotlib.pyplot as plt
plt.plot(range(max(crabs)), fuel)
plt.show()