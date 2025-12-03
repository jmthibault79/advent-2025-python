import sys
from util.input_reader import read_all_input

# parse ranges and find "invalid IDs" which consist of a pair of duplicated number sequences, e.g. 175175


def parse_input(argv: list[str]) -> list[tuple[str, str]]:
    """
    parse input file into a list of number string pairs
    """
    return [pair.split("-") for pair in read_all_input(argv).split(",")]


def is_invalid(num_str: str) -> bool:
    if len(num_str) % 2 != 0:
        return False
    else:
        half = len(num_str) // 2
        left = num_str[:half]
        right = num_str[half:]
        return left == right


def min_num_str(digits: int) -> str:
    return str(10 ** (digits - 1))


def max_num_str(digits: int) -> str:
    return str((10**digits) - 1)


def clamp_range(x: str, y: str) -> tuple[str, str] | None:
    """
    reduce a raw range into the smaller range which may contain invalid IDs, if possible
    """
    match len(x), len(y):
        case a, b if a == b and a % 2 == 0:
            # even and equal: good as-is
            return x, y
        case a, b if a == b and a % 2 != 0:
            # odd and equal: contains none
            return None
        case a, b if a != b and a % 2 == 0 and b == a + 1:
            # even first: clamp to max(even)
            return x, max_num_str(a)
        case a, b if a != b and a % 2 != 0 and b == a + 1:
            # odd first: clam to min(even)
            return min_num_str(b), y
        case a, b:
            raise Exception(
                f"Didn't account for the case of lengths {a}, {b} from {x}, {y}"
            )


def get_all_invalid(_range: tuple[str, str]) -> list[int]:
    left, right = _range[0], _range[1]
    left_len = len(left)
    right_len = len(right)
    assert left_len == right_len
    assert left_len % 2 == 0

    acc = []
    half_len = left_len // 2
    left_high_half, right_high_half = left[:half_len], right[:half_len]
    left_int, right_int = int(left), int(right)

    for i in range(int(left_high_half), int(right_high_half) + 1):
        dbl_str = f"{i}{i}"
        dbl_str_int = int(dbl_str)
        if dbl_str_int >= left_int and dbl_str_int <= right_int:
            acc.append(dbl_str_int)

    return acc


def main():
    input = parse_input(sys.argv)
    _part1(input)
    _part2(input)


def part1():
    input = parse_input(sys.argv)
    _part1(input)


def _part1(input: list[tuple[str, str]]):
    acc = []
    for line in input:
        clamped = clamp_range(line[0], line[1])
        if clamped:
            acc.extend(get_all_invalid(clamped))
    print(sum(acc))


def part2():
    input = parse_input(sys.argv)
    _part2(input)


def _part2(input: list[tuple[str, str]]):
    print("implement me")
