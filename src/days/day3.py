import sys
from util.input_reader import read_lines
from util.lists import list_to_int


def parse_input(argv: list[str]) -> list[list[int]]:
    return [[int(n) for n in line.strip()] for line in read_lines(argv)]


def joltage_2(line: list[int]) -> int:
    d1 = max(line[:-1])  # first digit can't be at the very end of the line
    d1_pos = line.index(d1)
    after_d1 = line[d1_pos + 1 :]
    d2 = max(after_d1)
    return d1 * 10 + d2


def joltage_n(line: list[int], n) -> int:
    if n == 1:
        return max(line)
    elif len(line) == n:
        return list_to_int(line)

    # standard case: len(line) > n > 1

    # get the largest value at the "start" of the line, meaning except for the last n-1 entries.
    # we know that it needs to be followed by n-1 digits
    except_end = line[: -n + 1]
    max_except_end = max(except_end)
    max_pos = line.index(max_except_end)
    rest = line[max_pos + 1 :]

    this_digit = (10 ** (n - 1)) * max_except_end
    other_digits = joltage_n(rest, n - 1)
    return this_digit + other_digits


def main():
    input = parse_input(sys.argv)
    _part1(input)
    _part2(input)


def part1():
    input = parse_input(sys.argv)
    _part1(input)


def _part1(input: list[list[int]]):
    print(sum([joltage_2(line) for line in input]))


def part2():
    input = parse_input(sys.argv)
    _part2(input)


def _part2(input):
    print(sum([joltage_n(line, 12) for line in input]))
