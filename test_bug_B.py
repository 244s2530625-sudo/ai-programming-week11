from bug3_logic import find_max


def test_find_max_single_value():
    assert find_max([7]) == 7


def test_find_max_when_largest_is_first():
    assert find_max([9, 3, 2]) == 9


def test_find_max_when_largest_is_middle():
    assert find_max([1, 9, 3]) == 9


def test_find_max_when_largest_is_last():
    assert find_max([1, 2, 9]) == 9
