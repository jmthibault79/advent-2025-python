import sys
import re
from util.input_reader import read_lines
from util.profiler import profile_function
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


def profile_d10p1():
    """Profile day 10 part 1"""
    profile_function(func=part1, argv=sys.argv[1:])


def parse_input(argv: list[str]) -> list[tuple[list[bool], list[list[int]], list[int]]]:
    reg = re.compile(r"\[(.*)\](.*?){(.*)}")
    acc = []
    for line in read_lines(argv):
        x = re.search(reg, line)
        if x is None:
            raise Exception("bad line", line)

        indicators = [char == "#" for char in x.group(1)]
        button_combos = [
            [int(button) for button in combo.strip("()").split(",")]
            for combo in x.group(2).split()
        ]
        joltage = [int(num) for num in x.group(3).split(",")]

        acc.append((indicators, button_combos, joltage))
    return acc


def can_create(indicators: list[bool], button: list[int]) -> bool:
    new_indicators = [False for _ in range(len(indicators))]
    for b in button:
        new_indicators[b] = True
    return new_indicators == indicators


def combine_button_combos(combos_to_combine: tuple[list[int]]) -> list[int]:
    combined = set(combos_to_combine[0])
    for combo in combos_to_combine[1:]:
        for button in combo:
            if button in combined:
                combined.remove(button)
            else:
                combined.add(button)
    return list(combined)


def fewest_button_combos(indicators: list[bool], combos: list[list[int]]) -> int:
    n = 1
    for button in combos:
        if can_create(indicators, button):
            return n

    max_count = 10  # arbitrary
    while n < max_count:
        n += 1
        for buttons in combinations(combos, n):
            if can_create(indicators, combine_button_combos(buttons)):
                return n
    return 0


def _part1(input: list[tuple[list[bool], list[list[int]], list[int]]]):
    print(sum([fewest_button_combos(line[0], line[1]) for line in input]))


def _part2(input: list[tuple[list[bool], list[list[int]], list[int]]]):
    print("implement me")
