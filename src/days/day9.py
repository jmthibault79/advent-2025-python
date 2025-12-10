import sys
from util.input_reader import read_lines
from itertools import combinations


def main():
    input = parse_input(sys.argv)
    _part1(input)
    _part2(input)


def part1():
    input = parse_input(sys.argv)
    _part1(input)


def part2():
    input = parse_input(sys.argv)
    _part2(input)


def parse_input(argv: list[str]) -> list[list[int]]:
    return [[int(x) for x in line.strip().split(",")] for line in read_lines(argv)]


def rect_area(a: list[int], b: list[int]) -> int:
    x = abs(a[0] - b[0]) + 1
    y = abs(a[1] - b[1]) + 1
    return x * y


def largest_rectangle(points: list[list[int]]) -> int:
    all_distances = [(rect_area(a, b), a, b) for a, b in combinations(points, 2)]
    return sorted(all_distances, key=lambda x: x[0])[-1][0]


def _part1(points: list[list[int]]):
    print(largest_rectangle(points))


def _part2(input):
    print("implement me")
