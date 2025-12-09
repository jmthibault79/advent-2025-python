import pytest
from days.day8 import dist, largest_clique_sizes
from math import sqrt

dist_testdata = [
    ([1, 2, 3], [1, 2, 3], 0),
    ([1, 2, 3], [4, 5, 6], sqrt(27)),
    ([4, 5, 6], [1, 2, 3], sqrt(27)),
    (
        [162, 817, 812],
        [425, 690, 689],
        sqrt((425 - 162) ** 2 + (817 - 690) ** 2 + (812 - 689) ** 2),
    ),
]

largest_clique_size_testdata = [
    (
        [
            ("a", "b"),
        ],
        2,
    ),
    (
        [
            ("a", "b"),
            ("b", "c"),
            ("d", "e"),
        ],
        6,
    ),
]


@pytest.mark.parametrize("a, b, expected", dist_testdata)
def test_dist(a, b, expected):
    assert dist(a, b) == expected


@pytest.mark.parametrize("edges, expected", largest_clique_size_testdata)
def test_clique_sizes(edges, expected):
    assert largest_clique_sizes(edges) == expected
