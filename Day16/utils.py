import json
import math

ID_LITERAL_VALUE = 4
ID_OPERATOR_VALUE = 6


def pretty_print(d):
    print(json.dumps(d, indent="  "))


def hex_to_bin(s):
    # checkout https://stackoverflow.com/a/4859937
    bs = "".join([bin(int(c, 16))[2:].zfill(4) for c in s])
    return bs


def bin_to_int(s):
    return int(s, 2)


def get_version_and_type(b):
    return bin_to_int(b[:3]), bin_to_int(b[3:6]), b[6:]  # version, type, rest


def parse_literal_value(b, ignore_padding=True):
    if len(b) < 5:
        assert "input may not be shorter than the length of a single path"

    lit_len = 0
    parts = ""
    for i in range(0, len(b), 5):
        is_last_group = b[i] == "0"
        part = b[i + 1:i + 5]
        parts += part
        lit_len += 5
        if is_last_group:
            break

    padding_bits = 0
    if not ignore_padding:
        # calculate how many bits were used as padding.
        # +2 as we already know that header doesn't fill an octet
        len_last_quartet = (lit_len + 2) % 4

        if 0 < len_last_quartet < 4:
            padding_bits = 4 - len_last_quartet

    rest = b[lit_len + padding_bits:]
    return bin_to_int(parts), rest


def parse_operator_value(b):
    length_type_id = b[0]
    has_subpackage_count = length_type_id == "1"

    nr = 11 if has_subpackage_count else 15
    count = bin_to_int(b[1:nr + 1])

    included = b[nr + 1:]
    excluded = ""
    if not has_subpackage_count:
        excluded = included[count:]
        included = included[:count]

    return included, excluded, has_subpackage_count, count


def parse_packet(b):
    version, typeID, rest = get_version_and_type(b)
    is_literal = typeID == ID_LITERAL_VALUE
    packet_info = {"version": version, "type": typeID, "is_literal": is_literal}

    if is_literal:
        i, rest = parse_literal_value(rest, ignore_padding=True)
        packet_info["literal"] = i

    else:
        rest, excluded, has_subpackage_count, count = parse_operator_value(rest)
        sub_packages = []
        while True:
            if len(rest) < 6 or (has_subpackage_count and len(sub_packages) >= count):
                break

            res, rest = parse_packet(rest)
            sub_packages.append(res)

        if has_subpackage_count:
            packet_info["sub_package_count"] = count
        packet_info["sub_packages"] = sub_packages

        if not has_subpackage_count:
            rest = excluded

    return packet_info, rest


def parse_packet_string(s):
    bs = hex_to_bin(s)
    r, _ = parse_packet(bs)
    return r


def sum_version_numbers(packet_info):
    sum = packet_info["version"]
    if (sub_packages := packet_info.get("sub_packages")) is not None:
        for packet in sub_packages:
            sum += sum_version_numbers(packet)
    return sum


def eval_package(package):
    if (lit := package.get("literal")) is not None:
        return lit

    values = [eval_package(p) for p in package["sub_packages"]]
    match package["type"]:
        case 0:
            return sum(values)
        case 1:
            return math.prod(values)
        case 2:
            return min(values)
        case 3:
            return max(values)
        case 5:
            return int(values[0] > values[1])
        case 6:
            return int(values[0] < values[1])
        case 7:
            return int(values[0] == values[1])
