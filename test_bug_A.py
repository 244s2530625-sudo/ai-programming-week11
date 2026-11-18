import pytest
from bug3_logic import find_max


@pytest.mark.parametrize(
    "scores, expected",
    [
        ([70, 85, 60, 95], 95),
        ([10, 20, 30], 30),
        ([95, 85, 70, 60], 95),
        ([5], 5),
    ],
)
def test_find_max(scores, expected):
    assert find_max(scores) == expected
