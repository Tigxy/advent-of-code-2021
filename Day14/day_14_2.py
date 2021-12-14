from collections import Counter, defaultdict

# Parsing input
with open("input.txt") as fh:
	template = list(fh.readline().strip())
	_ = fh.readline()
	rules = {tpl[0]: tpl[1] for line in fh if (tpl := line.strip().split(" -> "))}

# Create substrings of template that can be used as rules input
template = [template[i] + template[i+1] for i in range(len(template) - 1)]

tmpl = defaultdict(lambda: 0)
for k in template:
	tmpl[k] += 1

n_steps = 40
for i in range(1, n_steps + 1):
	items = list(tmpl.items()) # save in variable to modify dict inplace
	
	for k,v in items:
		c = rules[k]
				
		tmpl[k[0] + c] += 1 * v
		tmpl[c + k[1]] += 1 * v
			
		tmpl[k] -= v
		if tmpl[k] == 0:
			del tmpl[k]
			
# Count total number of characters included in the dict
char_count = defaultdict(lambda: 0)
for k, v in tmpl.items():
	char_count[k[0]] += v
	char_count[k[1]] += v

# Except beginning and ending, each character is accounted for twice, which we need to fix
char_count[template[0][0]] -= 1
char_count[template[-1][-1]] -= 1
char_count = {k: v / 2 for k, v in char_count.items()}
char_count[template[0][0]] += 1
char_count[template[-1][-1]] += 1

char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

print("Most frequent - least frequent = ", char_count[0][1] - char_count[-1][1])