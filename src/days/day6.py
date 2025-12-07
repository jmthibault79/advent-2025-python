import sys
from util.input_reader import parse_columns, read_chars
from math import prod
from util.lists import list_to_int


def main():
    p1_cols = parse_columns(sys.argv)
    _part1(p1_cols)
    p2_chars = read_chars(sys.argv)
    _part2(p2_chars)


def part1():
    p1_cols = parse_columns(sys.argv)
    _part1(p1_cols)


def part2():
    p2_chars = read_chars(sys.argv)
    _part2(p2_chars)


def get_operator(op_str: str):
    match op_str:
        case "+":
            op = sum
        case "*":
            op = prod
        case other:
            raise Exception(f"operator '{other}' not expected")
    return op


def operate_p1(col: list[str]) -> int:
    op = get_operator(col[-1])
    return op([int(val) for val in col[:-1]])


def operate_p2(chars: list[list[str]], op, op_pos: int, next_op_pos: int) -> int:
    operands = []
    for col in range(op_pos, next_op_pos):
        operand_as_list = []
        for row in chars[:-1]:
            digit = row[col]
            if digit != " ":
                operand_as_list.append(int(digit))
        match len(operand_as_list):
            case 1:
                operands.append(operand_as_list[0])
            case n if n > 1:
                operands.append(list_to_int(operand_as_list))
    return op(operands)


def _part1(cols: list[list[str]]):
    print(sum([operate_p1(col) for col in cols]))


def _part2(chars: list[list[str]]):
    operator_line = chars[-1]

    op_cursor = 0
    acc = 0
    longest_row_len = max([len(row) for row in chars])
    while op_cursor < longest_row_len:
        op = get_operator(operator_line[op_cursor])
        next_op_pos = op_cursor + 1
        while next_op_pos < longest_row_len and operator_line[next_op_pos] == " ":
            next_op_pos += 1
        acc += operate_p2(chars, op, op_cursor, next_op_pos)
        op_cursor = next_op_pos

    print(acc)
