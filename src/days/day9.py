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
    width = abs(a[0] - b[0]) + 1
    height = abs(a[1] - b[1]) + 1
    return width * height


def largest_rectangle(points: list[list[int]]) -> int:
    all_distances = [(rect_area(a, b), a, b) for a, b in combinations(points, 2)]
    return sorted(all_distances, key=lambda x: x[0])[-1][0]


def _part1(points: list[list[int]]):
    print(largest_rectangle(points))


def build_path(red_points: list[list[int]]) -> list[list[int]]:
    first_point = red_points[0]
    points_plus_first_again = list(red_points)
    points_plus_first_again.append(first_point)
    path = []

    for idx, point in enumerate(points_plus_first_again[1:]):
        prev_point = red_points[idx]
        match point, prev_point:
            case a, b if a[0] == b[0] and a[1] > b[1]:
                # add path right: [prev_point, point)
                path.extend([[a[0], col] for col in range(b[1], a[1])])
            case a, b if a[0] == b[0] and a[1] < b[1]:
                # add path left: [prev_point, point)
                path.extend([[a[0], col] for col in range(b[1], a[1], -1)])
            case a, b if a[1] == b[1] and a[0] > b[0]:
                # add path up: [prev_point, point)
                path.extend([[row, a[1]] for row in range(b[0], a[0])])
            case a, b if a[1] == b[1] and a[0] < b[0]:
                # add path up: [prev_point, point)
                path.extend([[row, a[1]] for row in range(b[0], a[0], -1)])
    return path


def largest_red_green_rectangle(points: list[list[int]]) -> int:
    path = build_path(points)
    print(points)
    print(path)
    return len(path)


def _part2(points: list[list[int]]):
    print(largest_red_green_rectangle(points))
