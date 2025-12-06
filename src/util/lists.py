def list_to_int(li: list[int]) -> int:
    """
    Convert [1, 2, 3] to 123
    """
    acc, rest = li[0], li[1:]
    while len(rest) > 0:
        next, rest = rest[0], rest[1:]
        acc = acc * 10 + next
    return acc


def pad_to_length(li: list, value, desired_length: int) -> list:
    count = desired_length - len(li)
    if count <= 0:
        return li
    else:
        return li + [value] * count
