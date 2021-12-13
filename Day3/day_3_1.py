import numpy as np


with open("input.txt", "r") as fh:
    values = [[int(c) for c in line.strip()] for line in fh.readlines()]
   
values = np.array(values)

n = len(values)
digit_sum = values.sum(axis=0)

gamma_rate = (digit_sum > n//2).astype(np.int32)
epsilon_rate = (digit_sum < n//2).astype(np.int32)

gamma = gamma_rate.dot(2 ** np.arange(values.shape[1])[::-1])
epsilon = epsilon_rate.dot(2 ** np.arange(values.shape[1])[::-1])

print(digit_sum)
print(n // 2)

print("Gamma:", epsilon)
print("Epsilon:", gamma)
print("Product:",  epsilon * gamma)

