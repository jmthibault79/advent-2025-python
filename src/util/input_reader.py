def parse_input_filename(argv: list[str]) -> str | None:
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

    file_type = input[0]
    if file_type != "i" and file_type != "s":
        raise Exception("Expected input or sample file argument")

    match file_type:
        case "i":
            file_name = f"inputs/{input}.txt"
        case "s":
            file_name = f"sample_inputs/{input}.txt"

    return file_name


def read_all_input(argv: list[str]) -> str:
    """
    read an input or sample file and return the entire contents.
    """
    with open(parse_input_filename(argv), "r") as file:
        return file.read()


def parse_int_list_pair(file_name: str) -> tuple[list[int], list[int]]:
    """
    parse input as a pair of vertical integer lists, separated by some amount of whitespace
    """
    a, b = [], []
    with open(file_name, "r") as file:
        for line in file:
            split_line = line.split()
            # file ends in empty line
            if len(split_line) < 2:
                break
            a.append(int(split_line[0]))
            b.append(int(split_line[-1]))
    return a, b
