with open("input.txt", "r") as fh:
	values = [int(l) for l in fh.readlines()]
	
n_increases = 0
window_size = 3

prev_v = sum(values[:window_size])
for i in range(1, len(values) - (window_size - 1)):
	v = sum(values[i:i+window_size])
	if v > prev_v:
		n_increases += 1
	prev_v = v
	
print("n increases:", n_increases)
	