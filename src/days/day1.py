import sys
from util.input_reader import parse_input_filename
from collections import Counter

# start at position 50 (from 0-99)
# rotate left or right an integer amount
# p1: how many times do we hit 0?


def main():
    locations = parse(sys.argv)
    _part1(locations)
    _part2()


def parse(argv: list[str]) -> list[int]:
    """
    return a list of the positions where we stopped
    """
    file_name = parse_input_filename(argv)

    curr = 50
    acc = []

    with open(file_name, "r") as file:
        for line in file:
            first = line[0]
            match first:
                case "R":
                    curr = (curr + int(line[1:])) % 100
                    acc.append(curr)
                case "L":
                    curr = (curr - int(line[1:])) % 100
                    acc.append(curr)
    return acc


def part1():
    locations = parse(sys.argv)
    _part1(locations)


def _part1(locations: list[int]):
    print(Counter(locations)[0])


def part2():
    _part2()


def _part2():
    print("N/A")
