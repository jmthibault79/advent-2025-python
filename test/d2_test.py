import pytest

from days.day2 import is_invalid, clamp_range, get_all_invalid

is_invalid_testdata = [
    ("0", False),
    ("9", False),
    ("10", False),
    ("11", True),
]

clamp_range_testdata = [
    ("1", "1", None),
    ("10", "10", ("10", "10")),
    ("50", "123", ("50", "99")),
    ("789", "1010", ("1000", "1010")),
    ("12345", "78978", None),
]

get_all_invalid_testdata = [
    (("11", "22"), [11, 22]),
    (("10", "30"), [11, 22]),
    (("1000", "1011"), [1010]),
    (("1234", "1575"), [1313, 1414, 1515]),
]


@pytest.mark.parametrize("num_str, expected", is_invalid_testdata)
def test_is_invalid(num_str, expected):
    assert is_invalid(num_str) == expected


@pytest.mark.parametrize("a, b, expected", clamp_range_testdata)
def test_clamp_range(a, b, expected):
    assert clamp_range(a, b) == expected


@pytest.mark.parametrize("_range, expected", get_all_invalid_testdata)
def test_get_all_invalid(_range, expected):
    assert get_all_invalid(_range) == expected
