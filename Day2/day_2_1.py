hor_pos, depth = 0, 0

with open("input.txt", "r") as fh:
	for line in fh:
		cmd, value = line.strip().split(" ")
		value = int(value)
		
		if cmd == "forward":
			hor_pos += value
		elif cmd == "down": 
			depth += value
		else:
			depth -= value

print("Horizontal Position", hor_pos)
print("Depth", depth)
print("Results multiplied", hor_pos * depth)