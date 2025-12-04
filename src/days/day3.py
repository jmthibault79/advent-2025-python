import sys
from util.input_reader import read_lines


def parse_input(argv: list[str]) -> list[list[int]]:
    return [[int(n) for n in line.strip()] for line in read_lines(argv)]


def highest_joltage(line: list[int]) -> int:
    d1 = max(line[:-1])  # first digit can't be at the very end of the line
    d1_pos = line.index(d1)
    after_d1 = line[d1_pos + 1 :]
    d2 = max(after_d1)
    return d1 * 10 + d2


def main():
    input = parse_input(sys.argv)
    _part1(input)
    _part2(input)


def part1():
    input = parse_input(sys.argv)
    _part1(input)


def _part1(input: list[list[int]]):
    print(sum([highest_joltage(line) for line in input]))


def part2():
    input = parse_input(sys.argv)
    _part2(input)


def _part2(input):
    print("implement me")
