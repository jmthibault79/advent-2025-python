import sys
from util.input_reader import read_lines
from itertools import combinations, groupby


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
    width = abs(a[0] - b[0]) + 1
    height = abs(a[1] - b[1]) + 1
    return width * height


def largest_rectangle(points: list[list[int]]) -> int:
    all_areas = [(rect_area(a, b), a, b) for a, b in combinations(points, 2)]
    return sorted(all_areas, key=lambda x: x[0])[-1][0]


def _part1(points: list[list[int]]):
    print(largest_rectangle(points))

def rect_area_without_points_inside(a: list[int], b: list[int], grouped_points: dict[int,list[int]]) -> int:
    # never mind, this is invalid anyway
    # there exist some invalid rectangles without points inside
    # like AB here
    # A--x
    # |  | x-B
    # |  | | |
    # |  x-x |
    # x------x

    return 0

def largest_red_green_rectangle(points: list[list[int]]) -> int:
    sorted_by_row = sorted(points, key=lambda x: x[0])
    grouped_by_row = {
        row: sorted([point[1] for point in points])
        for row, points in groupby(sorted_by_row, key=lambda x: x[0])
    }

    # for each pair, are there any points inside?  if no: get area 
    all_areas = [(rect_area_without_points_inside(a, b, grouped_by_row), a, b) for a, b in combinations(points, 2)]
    return sorted(all_areas, key=lambda x: x[0])[-1][0]

def _part2(points: list[list[int]]):
    print(largest_red_green_rectangle(points))
