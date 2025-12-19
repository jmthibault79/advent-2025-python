import sys
from util.input_reader import read_lines


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


def parse_input(argv: list[str]) -> dict[str, list[str]]:
    graph = {}
    for line in read_lines(argv):
        device, outputs = line.split(":")
        graph[device] = outputs.strip().split(" ")
    return graph


start = "you"
end = "out"


def next_step(graph: dict[str, list[str]], path_so_far: list[str]) -> list[list[str]]:
    new_paths = []
    for output in graph[path_so_far[-1]]:
        new_path = list(path_so_far)
        new_path.append(output)
        if output == end:
            new_paths.append(new_path)
        elif output in path_so_far:
            continue
        else:
            next_paths = next_step(graph, new_path)
            if next_paths:
                new_paths.extend(next_paths)
    return new_paths


def _part1(graph: dict[str, list[str]]):
    paths = next_step(graph, [start])
    print(len(paths))


def _part2(input):
    print("implement me")
