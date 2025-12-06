import pytest
from days.day5 import group_fresh


group_fresh_testdata = [
    ([[1, 2]], {1: 2}),
    ([[1, 2], [1, 3]], {1: 3}),
    ([[1, 2], [2, 3], [1, 4]], {1: 4}),
    ([[1, 4], [2, 3], [1, 2]], {1: 4}),
]


@pytest.mark.parametrize("fresh_ranges, expected", group_fresh_testdata)
def test_group_fresh(fresh_ranges, expected):
    assert group_fresh(fresh_ranges) == expected
