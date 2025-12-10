import sys
from util.input_reader import read_lines
from itertools import combinations
from collections import defaultdict


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


def point_indices(
    points: list[list[int]],
) -> tuple[dict[int, list[int]], dict[int, list[int]]]:
    """
    basically a groupby but I got tripped up by semantics so here's a bare-bones version
    """
    row_index = defaultdict(list)
    col_index = defaultdict(list)
    for row, col in points:
        row_index[row].append(col)
        col_index[col].append(row)
    return {k: sorted(v) for k, v in sorted(row_index.items(), key=lambda x: x[0])}, {
        k: sorted(v) for k, v in sorted(col_index.items(), key=lambda x: x[0])
    }


def red_green_only(
    a: list[int],
    b: list[int],
    row_index: dict[int, list[int]],
    col_index: dict[int, list[int]],
):
    min_row, max_row = (
        min(a[0], b[0]),
        max(a[0], b[0]),
    )
    min_col, max_col = (
        min(a[1], b[1]),
        max(a[1], b[1]),
    )

    # check for any strictly-inside points (edges are OK)

    for row in range(min_row + 1, max_row):
        cols_in_row = row_index.get(row)
        if cols_in_row is not None:
            if any([min_col < col < max_col for col in cols_in_row]):
                return False

    for col in range(min_col + 1, max_col):
        rows_for_col = col_index.get(col)
        if rows_for_col is not None:
            # if there are any strictly-inside points (edges are OK)
            if any([min_row < row < max_row for row in rows_for_col]):
                return False

    return True


def largest_red_green_rectangle(points: list[list[int]]) -> int:
    row_index, col_index = point_indices(build_path(points))
    all_areas = [(rect_area(a, b), a, b) for a, b in combinations(points, 2)]

    for rect_and_area in sorted(all_areas, key=lambda x: x[0], reverse=True):
        area, a, b = rect_and_area
        if red_green_only(a, b, row_index, col_index):
            print(a, b)
            return area
    return 0


def _part2(points: list[list[int]]):
    print(largest_red_green_rectangle(points))
