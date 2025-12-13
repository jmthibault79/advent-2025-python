import pytest
from days.day10 import fewest_button_combos

fewest_button_combos_testdata = [
    ([True], [[0]], 1),
    ([True, True], [[0], [1]], 2),
]


@pytest.mark.parametrize("indicators, combos, expected", fewest_button_combos_testdata)
def test_fewest_combos(indicators, combos, expected):
    assert fewest_button_combos(indicators, combos) == expected
