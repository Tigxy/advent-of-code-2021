import numpy as np


with open("input.txt", "r") as fh:
    values = [[int(c) for c in line.strip()] for line in fh.readlines()]
   
values = np.array(values)

n = len(values)
n_digits = values.shape[1]

def binary_to_int(x):
    return x.dot(2 ** np.arange(x.shape[0])[::-1])

rating = np.ones(n_digits, dtype=np.int32)
subset = values.copy()
for i in range(n_digits):
    n_ones = subset.sum(axis=0)[i]
    n_zeros = len(subset) - n_ones
    majority_value = 1 if n_ones >= n_zeros else 0
    
    rating[i] = majority_value
    mask = subset[:, i] == majority_value
    subset = subset[mask]
    if len(subset) == 1:
        rating = subset[0]
        break
print(rating)

oxigen = binary_to_int(rating)

rating = np.zeros(n_digits, dtype=np.int32)
subset = values.copy()
for i in range(n_digits):
    n_ones = subset.sum(axis=0)[i]
    n_zeros = len(subset) - n_ones
    minority_value = 1 if n_ones < n_zeros else 0
    
    rating[i] = minority_value
    mask = subset[:, i] == minority_value
    subset = subset[mask]
    if len(subset) == 1:
        rating = subset[0]
        break
print(rating)

co2 = binary_to_int(rating)

print("Oxigen:", oxigen)
print("CO2:", co2)
print("Product:", oxigen*co2)
