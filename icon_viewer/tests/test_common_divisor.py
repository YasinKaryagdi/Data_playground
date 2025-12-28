from icon_viewer.helper_functions import get_divisors, get_common_divisors
import pytest

# testing for one number
@pytest.mark.parametrize("x, expected", [
    (1, [1]),
    (3, [1, 3]),
    (8, [1, 2, 4, 8]),
    (15, [1, 3, 5, 15]),
    (28, [1, 2, 4, 7, 14, 28])
])

def test_get_divisors(x, expected):
    assert get_divisors(x) == expected

# testing for two numbers
@pytest.mark.parametrize("x, y, expected", [
    # test for when both numbers are the same
    (1, 1, [1]),

    # basic tests
    (3, 9, [1, 3]),
    (8, 12, [1, 2, 4]),
    (15, 25, [1, 5]),
    (80, 100, [1, 2, 4, 5, 10, 20]),

    # testing for two numbers where one is multiple of the other
    (80, 160, [1, 2, 4, 5, 8, 10, 16, 20, 40, 80]),

    # ensure that order doesn't matter
    (160, 80, [1, 2, 4, 5, 8, 10, 16, 20, 40, 80])
])

def test_get_common_divisors(x, y, expected):
    assert get_common_divisors(x, y) == expected
