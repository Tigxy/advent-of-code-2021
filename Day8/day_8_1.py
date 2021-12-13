from collections import Counter

segments_per_number = {
    0: 6,
    1: 2, 
    2: 5, 
    3: 5, 
    4: 4,
    5: 5,
    6: 6, 
    7: 3,
    8: 7,
    9: 6    
}

with open("input.txt") as fh:
    lines = [(s[:-5], s[-4:])  for line in fh if (s := line.strip().split(" "))]
    
def sort_str(s):
    a = sorted(list(s))
    return "".join(a)
 
outputs = [len(sort_str(d)) for i, o in lines for d in o]
counter = Counter(outputs)
print(counter)

a = [1,4,7,8]
for i in a:
    print("Number", i, counter[segments_per_number[i]])