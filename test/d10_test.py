import pytest
from days.day10 import (
    combine_buttons_1,
    can_create_1,
    fewest_buttons_1,
    button_to_joltage,
    Indicators,
    Button,
    Joltage,
)

combine_buttons_1_testdata = [
    ([Button(b=[0]), Button(b=[1])], Button(b=[0, 1])),
    ([Button(b=[0, 1]), Button(b=[1, 2])], Button(b=[0, 2])),
    ([Button(b=[0, 4]), Button(b=[0, 1, 2]), Button(b=[1, 2, 3, 4])], Button(b=[3])),
]

can_create_1_testdata = [
    (Indicators(i=[False, False, False, True, False]), Button(b=[3]), True),
]

fewest_buttons_1_testdata = [
    (Indicators(i=[True]), [Button(b=[0])], 1),
    (Indicators(i=[True, True]), [Button(b=[0]), Button(b=[1])], 2),
    (
        Indicators(i=[False, False, False, True, False]),
        [
            Button(b=[0, 2, 3, 4]),
            Button(b=[2, 3]),
            Button(b=[0, 4]),
            Button(b=[0, 1, 2]),
            Button(b=[1, 2, 3, 4]),
        ],
        3,
    ),
    (
        Indicators(i=[False, False, False, True, False]),
        [
            Button(b=[0, 4]),
            Button(b=[0, 1, 2]),
            Button(b=[1, 2, 3, 4]),
        ],
        3,
    ),
]

to_joltage_testdata = [
    (
        Button(b=[0]),
        1,
        Joltage(j=(1,)),
    ),
    (Button(b=[0, 1]), 2, Joltage(j=(1, 1))),
    (Button(b=[0, 1]), 3, Joltage(j=(1, 1, 0))),
    # ((3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    # (Joltage(j=[3,5,4,7]), Button(b=[3]), False),
]


@pytest.mark.parametrize("buttons, expected", combine_buttons_1_testdata)
def test_combine_buttons_1(buttons, expected):
    assert combine_buttons_1(buttons) == expected


@pytest.mark.parametrize("indicators, button, expected", can_create_1_testdata)
def test_can_create_1(indicators, button, expected):
    assert can_create_1(indicators, button) == expected


@pytest.mark.parametrize("indicators, buttons, expected", fewest_buttons_1_testdata)
def test_fewest_buttons_1(indicators, buttons, expected):
    assert fewest_buttons_1(indicators, buttons) == expected


@pytest.mark.parametrize("button, toggle_count, expected", to_joltage_testdata)
def test_button_to_joltage(button, toggle_count, expected):
    assert button_to_joltage(button, toggle_count) == expected
