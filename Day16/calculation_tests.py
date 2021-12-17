from utils import *


test_cases = [
    ("C200B40A82", 3),
    ("04005AC33890", 54),
    ("880086C3E88112", 7),
    ("CE00C43D881120", 9),
    ("D8005AC2A8F0", 1),
    ("F600BC2D8F", 0),
    ("9C005AC2F8F0", 0),
    ("9C0141080250320F1802104A08", 1)
]


for s, v in test_cases:
    package = parse_packet_string(s)
    res = eval_package(package)

    print(res)
    assert v == res, "Failure for '%s'" % s
