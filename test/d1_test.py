import pytest

from days.day1 import go_right, go_left

right_pos_testdata = [
    (0, 1, 1),
    (10, 75, 85),
    (90, 10, 0),
    (90, 20, 10),
    (90, 120, 10),
    (50, 540, 90),
]

left_pos_testdata = [(1, 1, 0), (10, 5, 5), (10, 20, 90), (30, 220, 10), (40, 250, 90)]

right_zeros_testdata = [
    (0, 1, 0),
    (10, 10, 0),
    (50, 50, 1),
    (10, 500, 5),
    (0, 100, 1),
    (0, 500, 5),
    (90, 510, 6),
    (52, 48, 1),
    (95, 55, 1),
]

left_zeros_testdata = [
    (1, 1, 1),
    (10, 20, 1),
    (10, 5, 0),
    (0, 100, 1),
    (0, 500, 5),
    (10, 110, 2),
    (50, 68, 1),
    (82, 30, 0),
    (0, 5, 0),
    (55, 55, 1),
    (0, 1, 0),
]


@pytest.mark.parametrize("current, count, expected_end", right_pos_testdata)
def test_go_right_pos(current, count, expected_end):
    assert go_right(current, count)[0] == expected_end


@pytest.mark.parametrize("current, count, expected_end", left_pos_testdata)
def test_go_left_pos(current, count, expected_end):
    assert go_left(current, count)[0] == expected_end


@pytest.mark.parametrize("current, count, expected_zeros", right_zeros_testdata)
def test_go_right_zeros(current, count, expected_zeros):
    assert go_right(current, count)[1] == expected_zeros


@pytest.mark.parametrize("current, count, expected_zeros", left_zeros_testdata)
def test_go_left_zeros(current, count, expected_zeros):
    assert go_left(current, count)[1] == expected_zeros
