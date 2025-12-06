import sys
from util.input_reader import parse_int_list_pair
from collections import Counter

# "day 0" is actually day 1 from 2024, for practice


def main():
    a, b = parse(sys.argv)
    _part1(a, b)
    _part2(a, b)


def parse(argv: list[str]) -> tuple[list[int], list[int]]:
    return parse_int_list_pair(argv)


def part1():
    """
    sort the right and left lists, and add up the abs diff between l0,r0 ; l1,r1 ; etc
    """
    a, b = parse(sys.argv)
    _part1(a, b)


def _part1(a: list[int], b: list[int]):
    a.sort()
    b.sort()
    abs_diffs = [abs(an - b[idx]) for idx, an in enumerate(a)]
    print(sum(abs_diffs))


def part2():
    """
    take the frequency-dist of both lists, and return l0 * freq_l(l0) * freq_r(l0)
    """
    a, b = parse(sys.argv)
    _part2(a, b)


def _part2(a: list[int], b: list[int]):
    a_freq = Counter(a)
    b_freq = Counter(b)
    freq_products = [item * a_count * b_freq[item] for item, a_count in a_freq.items()]
    print(sum(freq_products))
