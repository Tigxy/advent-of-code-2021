with open("input.txt", "r") as fh:
	values = [int(l) for l in fh.readlines()]
	
n_increases = 0

prev_v = values[0]
for v in values[1:]:
	if v > prev_v:
		n_increases += 1
	prev_v = v
	
print("n increases:", n_increases)
	