from utils import *


test_cases = [
    ("38006F45291200", 9),
    ("EE00D40C823060", 14),
    ("8A004A801A8002F478", 16),
    ("620080001611562C8802118E34", 12),
    ("C0015000016115A2E0802F182340", 23),
    ("A0016C880162017C3686B18A3D4780", 31)
]


for s, v in test_cases:
    r = parse_packet_string(s)
    version_sum = sum_version_numbers(r)

    print()
    print("Sum is", version_sum, "Sum should be", v)

    assert v == version_sum, "Failure for '%s'" % s
