import sys
from util.input_reader import read_lines


def parse_input(argv: list[str]) -> tuple[list[list[int]], list[int]]:
    lines = read_lines(argv)
    fresh = []
    available = []
    reading_fresh_ranges = True
    for line in lines:
        if reading_fresh_ranges:
            if line.strip() == "":
                reading_fresh_ranges = False
            else:
                fresh.append([int(val) for val in line.split("-")])
        else:
            available.append(int(line))
    return fresh, available


def main():
    fresh, available = parse_input(sys.argv)
    _part1(fresh, available)
    _part2(fresh)


def part1():
    fresh, available = parse_input(sys.argv)
    _part1(fresh, available)


def _part1(fresh: list[list[int]], available: list[int]):
    count = 0
    for ing in available:
        for fresh_range in fresh:
            if ing >= fresh_range[0] and ing <= fresh_range[1]:
                count += 1
                break
    print(count)


def group_fresh(fresh_ranges: list[list[int]]) -> dict[int, int]:
    """
    Groups a list of fresh-ranges by sorted start value, combining with the next start value when appropriate
    """
    grouped = {}
    prev_group = None
    for fresh_range in sorted(fresh_ranges, key=lambda x: x[0]):
        start, end = fresh_range[0], fresh_range[1]
        if start in grouped:
            if grouped[start] < end:
                grouped[start] = end
        else:
            # start not present in grouped - combine with previous group or start a new one?
            # if no previous group -> new one
            # if grouped exists, check the previous group's end.  if equal or after this start, combine.  else create new group
            if not prev_group:
                grouped[start] = end
                prev_group = start
            else:
                prev_group_end = grouped[prev_group]
                if prev_group_end < start:
                    grouped[start] = end
                    prev_group = start
                else:
                    if prev_group_end < end:
                        grouped[prev_group] = end
    return grouped


def part2():
    fresh, _ = parse_input(sys.argv)
    _part2(fresh)


def _part2(fresh: list[list[int]]):
    grouped_fresh = group_fresh(fresh)
    print(sum(v - k + 1 for k, v in grouped_fresh.items()))
