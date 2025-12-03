import pytest

from days.day2 import (
    is_p1_invalid,
    clamp_range_p1,
    get_all_p1_invalid,
    split_range_p2,
    get_all_p2_invalid,
    get_step,
)

is_p1_invalid_testdata = [
    ("0", False),
    ("9", False),
    ("10", False),
    ("11", True),
]

clamp_range_p1_testdata = [
    ("1", "1", None),
    ("10", "10", ("10", "10")),
    ("50", "123", ("50", "99")),
    ("789", "1010", ("1000", "1010")),
    ("12345", "78978", None),
]

get_all_p1_invalid_testdata = [
    (("11", "22"), [11, 22]),
    (("10", "30"), [11, 22]),
    (("1000", "1011"), [1010]),
    (("1234", "1575"), [1313, 1414, 1515]),
]

split_range_p2_testdata = [
    ("1", "1", [("1", "1")]),
    ("10", "10", [("10", "10")]),
    ("50", "123", [("50", "99"), ("100", "123")]),
    ("789", "1010", [("789", "999"), ("1000", "1010")]),
    ("12345", "78978", [("12345", "78978")]),
]

get_step_testdata = [
    (2, 2, 101),  # 1212 + 101 = 1313
    (2, 3, 10101),  # 121212 + 10101 = 131313
    (3, 2, 1001),  # 123123 + 1001 = 124124
]

get_all_p2_invalid_testdata = [
    (("11", "22"), [11, 22]),
    (("10", "30"), [11, 22]),
    (("13", "33"), [22, 33]),
    (("100", "111"), [111]),
    (("123123122", "123123124"), [123123123]),
    (("222220", "222224"), [222222]),
]


@pytest.mark.parametrize("num_str, expected", is_p1_invalid_testdata)
def test_is_p1_invalid(num_str, expected):
    assert is_p1_invalid(num_str) == expected


@pytest.mark.parametrize("a, b, expected", clamp_range_p1_testdata)
def test_clamp_range_p1(a, b, expected):
    assert clamp_range_p1(a, b) == expected


@pytest.mark.parametrize("_range, expected", get_all_p1_invalid_testdata)
def test_get_all_p1_invalid(_range, expected):
    assert get_all_p1_invalid(_range) == expected


@pytest.mark.parametrize("a, b, expected", split_range_p2_testdata)
def test_split_range_p2(a, b, expected):
    assert split_range_p2(a, b) == expected


@pytest.mark.parametrize("seq_len, reps, expected", get_step_testdata)
def test_get_step(seq_len, reps, expected):
    assert get_step(seq_len, reps) == expected


@pytest.mark.parametrize("_range, expected", get_all_p2_invalid_testdata)
def test_get_all_p2_invalid(_range, expected):
    assert get_all_p2_invalid(_range) == expected
