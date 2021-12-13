from collections import Counter

with open("input.txt") as fh:
	days = [int(c) for c in fh.read().strip().split(",")]

counter = Counter(days)
print(counter)

n_days_reset = 6
n_days_born = n_days_reset + 2
n_days_sim = 256
for i in range(n_days_sim):
	counter = {k-1: v for k, v in counter.items()}	
	n_expired = counter.pop(-1, None)
	if n_expired:
		counter[n_days_born] = n_expired
		
		prev = counter.get(n_days_reset)
		counter[n_days_reset] = n_expired + (prev if prev else 0)
	print(sum(list(counter.values())), counter)
	
print(counter)
print("N fishes after", n_days_sim, "days:", sum(list(counter.values())))