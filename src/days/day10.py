import sys
import re
from util.input_reader import read_lines
from util.profiler import profile_function
from itertools import combinations_with_replacement
from pydantic import BaseModel
from typing import Tuple


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


class Indicators(BaseModel):
    i: list[bool]


class Button(BaseModel):
    b: list[int]


class Joltage(BaseModel, frozen=True):
    j: Tuple[int, ...]


class CombinedJoltage(BaseModel, frozen=True):
    j: Joltage
    count: int


def parse_input(argv: list[str]) -> list[tuple[Indicators, list[Button], Joltage]]:
    reg = re.compile(r"\[(.*)\](.*?){(.*)}")
    acc = []
    for line in read_lines(argv):
        x = re.search(reg, line)
        if x is None:
            raise Exception("bad line", line)

        indicators = Indicators(i=[char == "#" for char in x.group(1)])
        buttons = [
            Button(b=[int(toggle) for toggle in toggles.strip("()").split(",")])
            for toggles in x.group(2).split()
        ]
        joltage = Joltage(j=tuple([int(num) for num in x.group(3).split(",")]))

        acc.append((indicators, buttons, joltage))
    return acc


def can_create_1(indicators: Indicators, button: Button) -> bool:
    new_indicators = [False for _ in range(len(indicators.i))]
    for toggle in button.b:
        new_indicators[toggle] = True
    return new_indicators == indicators.i


def combine_buttons_1(buttons_to_combine: list[Button]) -> Button:
    combined = set(buttons_to_combine[0].b)
    for button in buttons_to_combine[1:]:
        for toggle in button.b:
            if toggle in combined:
                combined.remove(toggle)
            else:
                combined.add(toggle)
    return Button(b=list(combined))


def fewest_buttons_1(indicators: Indicators, buttons: list[Button]) -> int:
    n = 1
    for button in buttons:
        if can_create_1(indicators, button):
            return n

    # like a google quota: need some limit in place, but if we hit it, we lift it
    max_count = 9
    while n < max_count:
        n += 1
        for combo in combinations_with_replacement(buttons, n):
            if can_create_1(indicators, combine_buttons_1(combo)):
                return n

    raise Exception(f"{max_count} was not enough")


def _part1(input: list[tuple[Indicators, list[Button], Joltage]]):
    print(sum([fewest_buttons_1(line[0], line[1]) for line in input]))


def button_to_joltage(button: Button, toggle_count: int) -> Joltage:
    new_joltage = [0 for _ in range(toggle_count)]
    for toggle in button.b:
        new_joltage[toggle] += 1
    return Joltage(j=tuple(new_joltage))


def _part2(input: list[tuple[Indicators, list[Button], Joltage]]):
    pass
