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


def horizontal_segments(points: list[list[int]]) -> dict[int, list[tuple[int, int]]]:
    first_point = points[0]
    points_plus_first_again = list(points)
    points_plus_first_again.append(first_point)
    segments = defaultdict(list)

    for idx, point in enumerate(points_plus_first_again[1:]):
        prev_point = points[idx]

        # if points are in the same row, add to horiz-segments
        if point[0] == prev_point[0]:
            segments[point[0]].append(
                (min(point[1], prev_point[1]), max(point[1], prev_point[1]))
            )

    return {k: v for k, v in sorted(segments.items(), key=lambda x: x[0])}


def max_histogram_area(row: list[int]) -> int:
    max_val = max_input = max(row)

    # todo: better algorithm than this?
    for i in range(1, max_input + 1):
        run_sum = 0
        for col in row:
            if col >= i:
                run_sum += i
            else:
                max_val = max(max_val, run_sum)
                run_sum = 0
        max_val = max(max_val, run_sum)

    return max_val


def largest_red_green_rectangle(points: list[list[int]]) -> int:
    """
    use a modified version of the "max area in a histogram" algorithm

    top row: record 0 for empty grid spaces, 1 for part of a segment
    record max-hist-area of the row as largest-rectangle

    for each row after, record 0 for outside, 1+above row for inside
    largest-rectangle = max(largest-rectangle, max-hist-area of the row)
    *** but only if the rectangle has a corner on a segment ***

    """
    height = max([point[0] for point in points]) + 1
    width = max([point[1] for point in points]) + 1

    print(height, width)

    hs = horizontal_segments(points)
    hs_rows = [k for k in hs]

    first_segment_row = hs_rows[0]
    segments = hs[first_segment_row]

    hist_counter = [0 for _ in range(width)]
    for s in segments:
        for col in range(s[0], s[1] + 1):
            hist_counter[col] = 1

    print("hs", hs)
    print("hs_rows", hs_rows)

    print(
        first_segment_row,
        "hist_counter",
        hist_counter,
        max_histogram_area(hist_counter),
    )

    prev_hist_counter = list(hist_counter)
    prev_segment_row = first_segment_row

    for segment_row in hs_rows[1:]:
        row_diff = segment_row - prev_segment_row
        segments = hs[segment_row]
        hist_counter = [0 if col == 0 else col + row_diff for col in prev_hist_counter]
        for s in segments:
            for col in range(s[0], s[1] + 1):
                if prev_hist_counter[col] == 0:
                    hist_counter[col] = 1

        print(
            segment_row, "hist_counter", hist_counter, max_histogram_area(hist_counter)
        )
        prev_hist_counter = list(hist_counter)
        prev_segment_row = segment_row

    return len(hs)


def _part2(points: list[list[int]]):
    print(largest_red_green_rectangle(points))
