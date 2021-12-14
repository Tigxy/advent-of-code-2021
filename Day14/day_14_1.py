from collections import Counter

with open("input.txt") as fh:
	template = list(fh.readline().strip())
	_ = fh.readline()
	rules = {tpl[0]: tpl[1] for line in fh if (tpl := line.strip().split(" -> "))}

n_steps = 10
for i in range(1, n_steps + 1):
	k = 0
	while k < len(template) - 1:
		insertion = rules[template[k] + template[k+1]]
		template.insert(k+1, insertion)
		k += 2

count = Counter(template)
count = sorted(count.items(), key=lambda x: x[1], reverse=True)
print(count)

print("Most frequent - least frequent = ", count[0][1] - count[-1][1])