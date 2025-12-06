def parse_input_filename(argv: list[str]) -> str:
    """
    parse an input or sample file indicator.
    """
    if len(argv) < 2:
        raise Exception("Expected a command argument to indicate input file")

    input = argv[1]
    if len(input) < 2:
        raise Exception(
            "Expected at least 2 chars: input or sample file, followed by the numerical choice of argument"
        )

    match input[0]:
        case "i":
            file_name = f"inputs/{input}.txt"
        case "s":
            file_name = f"sample_inputs/{input}.txt"
        case _:
            raise Exception("Expected input or sample file argument")

    return file_name


def read_all_input(argv: list[str]) -> str:
    """
    read an input or sample file and return the entire contents.
    """
    with open(parse_input_filename(argv), "r") as file:
        return file.read()


def read_lines(argv: list[str]) -> list[str]:
    """
    read an input or sample file and return each line in a list.
    """
    with open(parse_input_filename(argv), "r") as file:
        return [line for line in file]


def parse_columns(argv: list[str]) -> list[list[str]]:
    """
    parse input as columns of strings, separated by some amount of whitespace
    """
    num_cols = None
    with open(parse_input_filename(argv), "r") as file:
        for line in file:
            split_line = line.split()
            match len(split_line):
                case 0:
                    # don't try to parse an empty line
                    break
                case n if not num_cols:
                    num_cols = n
                    acc = [[] for i in range(n)]
                case n if n != num_cols:
                    raise Exception(
                        f"line has {n} columns, expected {num_cols}: {line}"
                    )

            for idx, val in enumerate(split_line):
                acc[idx].append(val)
    return acc


def parse_int_list_pair(argv: list[str]) -> tuple[list[int], list[int]]:
    """
    parse input as a pair of vertical integer lists, separated by some amount of whitespace
    """

    cols = parse_columns(argv)
    if len(cols) != 2:
        raise Exception(f"Unexpected number of columns in input: {len(cols)}")

    return [int(val) for val in cols[0]], [int(val) for val in cols[1]]
