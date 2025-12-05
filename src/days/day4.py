import sys
from util.input_reader import read_lines

roll = "@"
not_roll = "."


def parse_map(input: list[str]) -> list[list[int]]:
    acc = []
    for line in input:
        line_acc = []
        for char in line:
            if char == roll:
                line_acc.append(1)
            elif char == not_roll:
                line_acc.append(0)
        acc.append(line_acc)
    return acc


def augment_input_map(raw_map: list[list[int]]) -> list[list[int]]:
    """
    augment the raw input map with a buffer of empty spaces
    """
    raw_map_cols = len(raw_map[0])
    top_and_bottom = [0 for i in range(raw_map_cols + 2)]

    augmented_map = [top_and_bottom]
    augmented_map.extend([[0, *[val for val in line], 0] for line in raw_map])
    augmented_map.append(top_and_bottom)
    return augmented_map


def map_to_adjacency(aug_map: list[list[int]]) -> list[list[int]]:
    acc = []
    for aug_row, row_vals in enumerate(aug_map[1:-1]):
        orig_row = aug_row + 1
        row_acc = []
        for aug_col, _ in enumerate(row_vals[1:-1]):
            orig_col = aug_col + 1

            above = aug_map[orig_row - 1][orig_col - 1 : orig_col + 2]
            left = aug_map[orig_row][orig_col - 1]
            right = aug_map[orig_row][orig_col + 1]
            below = aug_map[orig_row + 1][orig_col - 1 : orig_col + 2]

            row_acc.append(sum(above) + left + right + sum(below))
        acc.append(row_acc)
    return acc


def parse_input(argv: list[str]) -> list[list[int]]:
    return parse_map(read_lines(argv))


def main():
    raw_map = parse_input(sys.argv)
    _part1(raw_map)
    _part2(raw_map)


def part1():
    raw_map = parse_input(sys.argv)
    _part1(raw_map)


def _part1(raw_map: list[list[int]]):
    adjacency = map_to_adjacency(augment_input_map(raw_map))
    fewer_than_4 = 0
    for row, row_vals in enumerate(raw_map):
        for col, col_val in enumerate(row_vals):
            if col_val == 1 and adjacency[row][col] < 4:
                fewer_than_4 += 1

    print(fewer_than_4)


def part2():
    raw_map = parse_input(sys.argv)
    _part2(raw_map)


def _part2(raw_map: list[list[int]]):
    print("implement me")
