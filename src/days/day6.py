import sys
from util.input_reader import parse_columns
from math import prod


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


def parse_input(argv: list[str]) -> list[list[str]]:
    return parse_columns(argv)


def operate(col: list[str]) -> int:
    match col[-1]:
        case "+":
            op = sum
        case "*":
            op = prod
        case other:
            raise Exception(f"operator '{other}' not expected")
    return op([int(val) for val in col[:-1]])


def _part1(cols: list[list[str]]):
    print(sum([operate(col) for col in cols]))


def _part2(input):
    print("implement me")
