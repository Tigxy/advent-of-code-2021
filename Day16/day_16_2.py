from utils import *

with open("input.txt") as fh:
    s = fh.read()

package = parse_packet_string(s)
r = eval_package(package)
print(r)  # correct result: 1725277876501
