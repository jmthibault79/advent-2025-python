import sys
from util.input_reader import read_lines
from itertools import combinations
from math import prod, sqrt


def main():
    input = parse_input(sys.argv)
    strings = parse_n(sys.argv)
    _part1(input, strings)
    _part2(input)


def part1():
    input = parse_input(sys.argv)
    strings = parse_n(sys.argv)
    _part1(input, strings)


def part2():
    input = parse_input(sys.argv)
    _part2(input)


# we are given N XYZ "junction box" coordinates. looks like each coordinate is betw 0 and 100K
# we're looking for the Q (s=10, i=1000) closest pairs, by euclidean distance
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


def add_point_to_cliques(
    clique_counter: int,
    clique_to_points: dict[int, list[str]],
    point_to_clique: dict[str, int],
    point_a: str,
    point_b: str,
) -> int:
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
    return clique_counter


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
        clique_counter = add_point_to_cliques(
            clique_counter, clique_to_points, point_to_clique, point_a, point_b
        )

    clique_counts = [len(points) for _, points in clique_to_points.items()]
    top_n = sorted(clique_counts, reverse=True)[:n]
    print(top_n)
    return prod(top_n)


def _part1(boxes: list[list[int]], strings: int):
    all_distances = [(dist(a, b), a, b) for a, b in combinations(boxes, 2)]
    top_n_distances = sorted(all_distances, key=lambda x: x[0])[:strings]
    print(largest_clique_sizes([(repr(a), repr(b)) for (_, a, b) in top_n_distances]))


def last_to_join_omniclique(
    edges: list[tuple[str, str]], point_count
) -> tuple[list[int], list[int]]:
    """
    Given an ordered collection of edges of a fully connected graph,
    which edge causes the final merging of cliques?

    Each connection between two junction boxes is an edge
    A circuit is a clique
    """

    clique_counter = 0
    clique_to_points: dict[int, list[str]] = {}
    point_to_clique: dict[str, int] = {}

    for point_a, point_b in edges:
        clique_counter = add_point_to_cliques(
            clique_counter, clique_to_points, point_to_clique, point_a, point_b
        )

        # we're done when there is only one clique and all points are in it
        if len(clique_to_points) == 1 and len(point_to_clique) == point_count:
            return (eval(point_a), eval(point_b))

    return ([0, 0, 0], [0, 0, 0])


def _part2(boxes: list[list[int]]):
    all_distances = [(dist(a, b), a, b) for a, b in combinations(boxes, 2)]
    sorted_by_dist = sorted(all_distances, key=lambda x: x[0])
    # I have not yet seen the TV show about the last to join the hive mind, so no spoilers pls
    pluribus_stragglers = last_to_join_omniclique(
        [(repr(a), repr(b)) for (_, a, b) in sorted_by_dist], len(boxes)
    )
    print(pluribus_stragglers)
    print(prod([x for x, *_ in pluribus_stragglers]))
