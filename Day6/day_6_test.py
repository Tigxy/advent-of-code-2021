import matplotlib.pyplot as plt
from collections import Counter

def sim(counter, n_days_sim, return_fish_counter=False):

	fish_counter = []

	n_days_reset = 6
	n_days_born = n_days_reset + 2
	for i in range(n_days_sim):
		counter = {k-1: v for k, v in counter.items()}	
		n_expired = counter.pop(-1, None)
		if n_expired:
			counter[n_days_born] = n_expired
			
			prev = counter.get(n_days_reset)
			counter[n_days_reset] = n_expired + (prev if prev else 0)
		fish_counter.append(sum(list(counter.values())))

	if return_fish_counter:
		return counter, fish_counter

	return counter

day_sim = {}
n_days_sim = 80
for i in range(8):
	_, day_sim[i] = sim({i: 1}, n_days_sim, True)
#print(day_sim)

fig, ax = plt.subplots()
for k, v in day_sim.items():
	ax.plot(range(n_days_sim), v, label=f"fish start with day={k}")
	
ax.legend()
ax.set_xlabel("days")
ax.set_ylabel("n fish")
plt.show()