import pytest
from days.day9 import rect_area, largest_rectangle

rect_area_testdata = [
    ([0, 0], [1, 1], 4),
]

largest_rectangle_testdata = [
    ([[0, 0], [1, 1]], 4),
]


@pytest.mark.parametrize("a, b, expected", rect_area_testdata)
def test_rect_area(a, b, expected):
    assert rect_area(a, b) == expected


@pytest.mark.parametrize("points, expected", largest_rectangle_testdata)
def test_largest_rectangle(points, expected):
    assert largest_rectangle(points) == expected
