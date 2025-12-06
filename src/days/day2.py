import sys
from util.input_reader import read_all_input

# p1: parse ranges and find "invalid IDs" which consist of a pair of duplicated number sequences, e.g. 175175
# p2: parse ranges and find "invalid IDs" which consist of N >= 2 of duplicated number sequences, e.g. 121212, 123123123


def parse_input(argv: list[str]) -> list[list[str]]:
    """
    parse input file into a list of number string pairs
    """
    return [pair.split("-") for pair in read_all_input(argv).split(",")]


def is_p1_invalid(num_str: str) -> bool:
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


def clamp_range_p1(x: str, y: str) -> tuple[str, str] | None:
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
            # odd first: clamp to min(even)
            return min_num_str(b), y
        case a, b:
            raise Exception(
                f"Didn't account for the case of lengths {a}, {b} from {x}, {y}"
            )


def split_range_p2(x: str, y: str) -> list[tuple[str, str]]:
    """
    split a raw range into ranges of the same length
    """
    match len(x), len(y):
        case a, b if a == b:
            # equal: good as-is
            return [(x, y)]
        case a, b if a != b and a % 2 == 0 and b == a + 1:
            # even first: clamp first to max(even)
            max_even = max_num_str(a)
            return [(x, max_even), (str(int(max_even) + 1), y)]
        case a, b if a != b and a % 2 != 0 and b == a + 1:
            # odd first: clamp last to min(even)
            min_even = min_num_str(b)
            return [(x, str(int(min_even) - 1)), (min_even, y)]
        case _:
            raise Exception(
                f"Didn't account for the case of lengths {len(x)}, {len(y)} from {x}, {y}"
            )


def get_all_p1_invalid(_range: tuple[str, str]) -> list[int]:
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


def get_step(seq_length: int, repetitions: int) -> int:
    """
    given a length of a number sequence and a number of repetitions, how long is the step between this one and the next?
    e.g. seq_length = 2, repetitions = 2 -> 1212, 1313, step = 101
    """
    acc = 1
    for rep in range(1, repetitions):
        acc = acc * 10**seq_length + 1
    return acc


def get_all_p2_invalid(_range: tuple[str, str]) -> list[int]:
    left, right = _range[0], _range[1]
    left_val, right_val = int(left), int(right)
    left_len = len(left)
    right_len = len(right)
    assert left_len == right_len

    acc = []

    # generate repeating values of length N from (1 to left_len // 2)
    for repeating_length in range(1, left_len // 2 + 1):
        # N needs to be evenly divisible by left_len
        if left_len % repeating_length != 0:
            continue

        repetitions = left_len // repeating_length
        left_prefix = left[:repeating_length]
        start_val = int(left_prefix * repetitions)
        step = get_step(repeating_length, repetitions)

        for val in range(start_val, right_val + 1, step):
            if val >= left_val and val <= right_val:
                acc.append(val)

    # dedupe the list
    # necessary because 222222 will appear 3x: 2,2,2,2,2,2;22,22,22;222,222
    return list(dict.fromkeys(acc))


def main():
    input = parse_input(sys.argv)
    _part1(input)
    _part2(input)


def part1():
    input = parse_input(sys.argv)
    _part1(input)


def _part1(input: list[list[str]]):
    acc = []
    for line in input:
        clamped = clamp_range_p1(line[0], line[1])
        if clamped:
            acc.extend(get_all_p1_invalid(clamped))
    print(sum(acc))


def part2():
    input = parse_input(sys.argv)
    _part2(input)


def _part2(input: list[list[str]]):
    acc = []
    for line in input:
        for same_length_range in split_range_p2(line[0], line[1]):
            acc.extend(get_all_p2_invalid(same_length_range))
    print(sum(acc))
