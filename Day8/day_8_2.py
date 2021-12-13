from collections import Counter, defaultdict

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

def set_join(*args):
    a = args[0]
    for b in args[1:]:
        a = a.union(b)
    return a
        
#  aaaa 
# b    c
# b    c
#  dddd 
# e    f
# e    f
#  gggg 

value_sum = 0
for i, o in lines   :
    i = [sort_str(_i) for _i in i]
    o = [sort_str(_o) for _o in o]
    ilen = [len(_i) for _i in i]
    
    counter = defaultdict(lambda: [])
    for i, _l in zip(i, ilen):
        counter[_l].append(i)
    counter = dict(counter)
    
    cf = set(counter[segments_per_number[1]][0])
    a = set(counter[segments_per_number[7]][0]) - cf
    bd = set(counter[segments_per_number[4]][0]) - cf

    for _i in counter[segments_per_number[9]]:
        g = set(list(_i)) - cf - a - bd
        if len(g) == 1:
            break

    e = set(counter[segments_per_number[8]][0]) - a - bd - cf - g

    for _i in counter[segments_per_number[6]]:
        f = set(list(_i)) - a - e - g - bd
        if len(f) == 1:
            break

    c = cf - f

    for _i in counter[segments_per_number[0]]:
        b = set(list(_i)) - a - cf - g - e
        if len(b) == 1:
            break
                
    d = bd - b
    
    print(a,b,c,d,e,f,g)
            
    value_table = {
        "".join(set_join(a, b, c, e, f, g)): "0",
        "".join(set_join(c, f)): "1",
        "".join(set_join(a, c, d, e, g)): "2",
        "".join(set_join(a, c, d, f, g)): "3",
        "".join(set_join(b, c, d, f)): "4",
        "".join(set_join(a, b, d, f, g)): "5",
        "".join(set_join(a, b, d, e, f, g)): "6",
        "".join(set_join(a, c, f)): "7",
        "".join(set_join(a, b, c, d, e, f, g)): "8",
        "".join(set_join(a, b, c, d, f, g)): "9"
    }
    value_table = {sort_str(k): v for k, v in value_table.items()}
 
    print(value_table)
    a = "".join([value_table[_o] for _o in o])
    nr = int(a)
    
    print("Number is:", nr)
    value_sum += nr
print("Sum is:", value_sum)