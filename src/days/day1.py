import sys
from util.input_reader import read_lines
from collections import Counter

# start at position 50 (from 0-99)
# rotate left or right an integer amount
# p1: how many times do we hit 0?


def go_right(curr: int, count: int) -> tuple[int, int]:
    """
    return the end position and the number of new times 0 was seen
    """
    raw_next = curr + count
    new_zeros, mod_next = raw_next // 100, raw_next % 100
    curr = mod_next

    return mod_next, new_zeros


def go_left(curr: int, count: int) -> tuple[int, int]:
    """
    return the end position and the number of new times 0 was seen
    """
    full_rotation_zeros = count // 100
    raw_next = curr - (count % 100)

    # there are no "rotate 0" instructions, so we don't need to account for that
    match raw_next, curr:
        case 0, 0:
            return raw_next, full_rotation_zeros
        case 0, _:
            return raw_next, full_rotation_zeros + 1
        case n, _ if n > 0:
            return raw_next, full_rotation_zeros
        case n, 0 if n < 0:
            return raw_next + 100, full_rotation_zeros
        case n, _ if n < 0:
            return raw_next + 100, full_rotation_zeros + 1


def rotate_all(curr: int, rotations: list[str]) -> list[tuple[int, int]]:
    acc = []
    for r in rotations:
        match [r[0], r[1:]]:
            case ["R", count]:
                curr, crossings = go_right(curr, int(count))
                acc.append((curr, crossings))
            case ["L", count]:
                curr, crossings = go_left(curr, int(count))
                acc.append((curr, crossings))
    return acc


def main():
    rotations = read_lines(sys.argv)
    locations = rotate_all(50, rotations)
    _part1(locations)
    _part2(locations)


def part1():
    rotations = read_lines(sys.argv)
    locations = rotate_all(50, rotations)
    _part1(locations)


def _part1(locations: list[tuple[int, int]]):
    print(Counter([end for end, _ in locations])[0])


def part2():
    rotations = read_lines(sys.argv)
    locations = rotate_all(50, rotations)
    _part2(locations)


def _part2(locations: list[tuple[int, int]]):
    print(sum([zeros for _, zeros in locations]))
