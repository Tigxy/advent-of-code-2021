from utils import *

with open("input.txt") as fh:
    s = fh.read()

r = parse_packet_string(s)
v = sum_version_numbers(r)

print(v)  # output is 927
