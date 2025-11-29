def read_input(argv: list[str]) -> str:
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

    with open(file_name, "r") as file:
        return file.read()
