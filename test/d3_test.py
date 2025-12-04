import pytest
from days.day3 import pack, joltage_n

pack_testdata = [([1], 1), ([9, 3], 93), ([3, 0, 2, 4, 7, 9], 302479)]

joltage_n_testdata = [
    ([1, 1], 2, 11),
    ([1, 2, 3], 2, 23),
    ([9, 4, 8, 0], 2, 98),
    ([1, 2, 3], 3, 123),
    ([1, 2, 3, 1, 2, 3], 3, 323),
    ([1, 2, 3, 1, 2, 3], 4, 3123),
    ([1, 2, 3, 1, 2, 3], 5, 23123),
]


@pytest.mark.parametrize("line, expected", pack_testdata)
def test_pack(line, expected):
    assert pack(line) == expected


@pytest.mark.parametrize("line, n, expected", joltage_n_testdata)
def test_joltage_n(line, n, expected):
    assert joltage_n(line, n) == expected
