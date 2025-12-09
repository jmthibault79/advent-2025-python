import sys
from util.input_reader import read_lines
from itertools import combinations
from math import prod, sqrt


def main():
    input = parse_input(sys.argv)
    strings = parse_n(sys.argv)
    _part1(input, strings)
    _part2(input, strings)


def part1():
    input = parse_input(sys.argv)
    strings = parse_n(sys.argv)
    _part1(input, strings)


def part2():
    input = parse_input(sys.argv)
    strings = parse_n(sys.argv)
    _part2(input, strings)


# we are given N XYZ "junction box" coordinates. looks like each coordinate is betw 0 and 100K
# we're looking for the Q (s=10, i=1000) closest pairs, by manhattan distance
# pairing up junc-boxes creates "circuits" which can keep growing as other JBs are added to the pile
# multiply the sizes of the 3 largest circuits

# I don't have any great ideas besides brute force yet, so let's try it


def parse_input(argv: list[str]) -> list[list[int]]:
    return [[int(v) for v in line.split(",")] for line in read_lines(argv)]


def parse_n(argv: list[str]) -> int:
    """
    The sample has 10 "strings" and the input has 1000
    """
    match argv[1][0]:
        case "i":
            return 1000
        case "s":
            return 10
        case _:
            raise Exception("Expected input or sample file argument")


def dist(a: list[int], b: list[int]) -> float:
    return sqrt(sum([(ai - bi) ** 2 for ai, bi in zip(a, b)]))


def largest_clique_sizes(edges: list[tuple[str, str]], n: int = 3) -> int:
    """
    Given a collection of edges, what are the sizes of the N largest cliques?

    Each connection between two junction boxes is an edge
    A circuit is a clique
    """
    clique_counter = 0
    clique_to_points: dict[int, list[str]] = {}
    point_to_clique: dict[str, int] = {}

    for point_a, point_b in edges:
        match point_to_clique.get(point_a), point_to_clique.get(point_b):
            case None, None:
                clique_to_points[clique_counter] = [point_a, point_b]
                point_to_clique[point_a] = clique_counter
                point_to_clique[point_b] = clique_counter
                clique_counter += 1
            case clique_a, clique_b if clique_a is None and clique_b is not None:
                point_to_clique[point_a] = clique_b
                clique_to_points[clique_b].append(point_a)
            case clique_a, clique_b if clique_a is not None and clique_b is None:
                point_to_clique[point_b] = clique_a
                clique_to_points[clique_a].append(point_b)
            case clique_a, clique_b if clique_a == clique_b:
                # nothing to do: both are already in the clique
                pass
            case clique_a, clique_b if clique_a != clique_b:
                # need to merge.  choose a arbitrarily
                b_points = clique_to_points[clique_b]
                for point in b_points:
                    point_to_clique[point] = clique_a
                clique_to_points[clique_a].extend(b_points)
                del clique_to_points[clique_b]

    clique_counts = [len(points) for _, points in clique_to_points.items()]
    top_n = sorted(clique_counts, reverse=True)[:n]
    print(top_n)
    return prod(top_n)


def _part1(boxes: list[list[int]], strings: int):
    all_distances = [(dist(a, b), a, b) for a, b in combinations(boxes, 2)]
    top_n_distances = sorted(all_distances, key=lambda x: x[0])[:strings]
    for top in top_n_distances:
        print(top)
    print(largest_clique_sizes([(str(a), str(b)) for (_, a, b) in top_n_distances]))


def _part2(boxes: list[list[int]], strings: int):
    print("implement me")
