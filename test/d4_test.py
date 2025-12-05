import pytest
from days.day4 import parse_map, augment_input_map, map_to_adjacency

parse_testdata = [
    ("@", [[1]]),
    (".", [[0]]),
    (
        [".@@", "@@.", "..."],
        [[0, 1, 1], [1, 1, 0], [0, 0, 0]],
    ),
]

augment_testdata = [
    ([[1]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
    ([[0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
    (
        [[0, 1, 1], [1, 0, 0], [0, 0, 0]],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ],
    ),
]

adjacency_testdata = [
    ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0]]),
    ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[8]]),
    (
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [2, 2, 1],
            [1, 3, 2],
            [1, 1, 0],
        ],
    ),
]


@pytest.mark.parametrize("input, expected", parse_testdata)
def test_parse_map(input, expected):
    assert parse_map(input) == expected


@pytest.mark.parametrize("in_map, expected", augment_testdata)
def test_augment(in_map, expected):
    assert augment_input_map(in_map) == expected


@pytest.mark.parametrize("aug_map, expected", adjacency_testdata)
def test_adjacency(aug_map, expected):
    assert map_to_adjacency(aug_map) == expected
