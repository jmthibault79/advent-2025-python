import pytest
from days.day9 import (
    rect_area,
    largest_rectangle,
    largest_red_green_rectangle,
)

rect_area_testdata = [
    ([0, 0], [1, 1], 4),
]

largest_rectangle_testdata = [
    ([[0, 0], [1, 1]], 4),
]

red_green_testdata = [
    ([[0, 0], [0, 2], [2, 2], [2, 0]], 9),
    # 4x3 is wrong here because it includes .
    # 3x3 is the best we can do in red-green mode
    # .#X#
    # ##XX
    # #XX#
    ([[0, 1], [0, 3], [2, 3], [2, 0], [1, 0], [1, 1]], 9),
]


@pytest.mark.parametrize("a, b, expected", rect_area_testdata)
def test_rect_area(a, b, expected):
    assert rect_area(a, b) == expected


@pytest.mark.parametrize("points, expected", largest_rectangle_testdata)
def test_largest_rectangle(points, expected):
    assert largest_rectangle(points) == expected


@pytest.mark.parametrize("points, expected", red_green_testdata)
def test_largest_red_green_rectangle(points, expected):
    assert largest_red_green_rectangle(points) == expected
