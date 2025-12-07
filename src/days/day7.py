import sys
from util.input_reader import read_chars


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


# insights from data exploration:
# 1. first row is only the start pos
# 2. second row, last row, and every row between splitters are empty
# 3. the right and left edge are spaces
# 4. the splitters are always separated by an odd number.
# equivalent: for each row, all are odd-cols or even-cols, and they never touch


def parse_input(argv: list[str]) -> list[list[str]]:
    return read_chars(sys.argv)


start_char = "S"
beam_char = "|"
splitter_char = "^"
space_char = "."


def pew_pew_pew(tachyon_manifold: list[list[str]]) -> tuple[int, int]:
    quantum_universe_counter = [[0 for _ in row] for row in tachyon_manifold]
    split_count = 0

    start_col = tachyon_manifold[0].index(start_char)
    tachyon_manifold[1][start_col] = beam_char
    quantum_universe_counter[1][start_col] = 1
    first_splitter_row = 2

    for row_idx_minus_offset, row_chars in enumerate(
        tachyon_manifold[first_splitter_row:]
    ):
        row_idx = row_idx_minus_offset + first_splitter_row
        for col_idx, col_char in enumerate(row_chars):
            if tachyon_manifold[row_idx - 1][col_idx] == beam_char:
                if col_char == splitter_char:
                    split_count += 1
                    prev_row, left_col, right_col = (
                        row_idx - 1,
                        col_idx - 1,
                        col_idx + 1,
                    )

                    tachyon_manifold[row_idx][left_col] = beam_char
                    quantum_universe_counter[row_idx][left_col] += (
                        quantum_universe_counter[prev_row][col_idx]
                    )

                    tachyon_manifold[row_idx][right_col] = beam_char
                    quantum_universe_counter[row_idx][right_col] += (
                        quantum_universe_counter[prev_row][col_idx]
                    )
                else:
                    tachyon_manifold[row_idx][col_idx] = beam_char
                    quantum_universe_counter[row_idx][col_idx] += (
                        quantum_universe_counter[row_idx - 1][col_idx]
                    )

    return split_count, sum(quantum_universe_counter[-1])


def _part1(tachyon_manifold: list[list[str]]):
    split_count, _ = pew_pew_pew(tachyon_manifold)
    print(split_count)


def _part2(tachyon_manifold: list[list[str]]):
    _, universe_count = pew_pew_pew(tachyon_manifold)
    print(universe_count)
