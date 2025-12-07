import pytest
from days.day7 import pew_pew_pew


quantum_testdata = [
    (
        [
            [".", "S", "."],
            [".", ".", "."],
            [".", "^", "."],
        ],
        2,
    ),
    (
        [
            [".", ".", "S", ".", "."],
            [".", ".", ".", ".", "."],
            [".", ".", "^", ".", "."],
            [".", ".", ".", ".", "."],
            [".", "^", ".", ".", "."],
        ],
        3,
    ),
    (
        [
            [".", ".", "S", ".", "."],
            [".", ".", ".", ".", "."],
            [".", ".", "^", ".", "."],
            [".", ".", ".", ".", "."],
            [".", "^", ".", "^", "."],
        ],
        4,
    ),
]


@pytest.mark.parametrize("tachyon_manifold, expected", quantum_testdata)
def test_quantum(tachyon_manifold, expected):
    _, quantum = pew_pew_pew(tachyon_manifold)
    assert quantum == expected
