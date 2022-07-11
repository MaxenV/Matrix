
import pytest
from matrix_lib import check_if_correct


@pytest.mark.parametrize(
    ("matrix_table"),
    (
        ([[4, 5, 2]]),
        (([0, 0, 0, 0], [0, 0, 0, 0], [0, -0, 0, 0], [0, 0, 0, 0])),
        (([0, 0, 0, 0], [0, 0, 0, 0], [0, -0, 0, 0], [0, 0, 0, 0])),
        ([[4, 4.6, 3, 5], [7, -8, 5, 7], [2, 7, 3, 1], [6, -3, 4, 5]]),
        ([[4, -4.6, 3, 5]]),
        ([[4, 5.64, 5]]),
    )
)
def test_check_correct_true(matrix_table):
    assert check_if_correct(matrix_table)


@pytest.mark.parametrize(
    ("matrix_table"),
    (
        ([[4, 5, 2], 4, 5, 7]),
        ([[4, 4.6, 3, 5], [7, 5, 7], [2, 7, 3, 1], [6, -3,  5]]),
        ([[4, 4.6, 3, 5], {7, 5, 7, 7}, [2, 7, 3, 1], [6, -3, 4,  5]]),
        ([[4, -4.6, "3", 5]]),
        ([[True, 5.64, 5]]),
        ([[76, 5.64, False]]),
    )
)
def test_check_correct_false(matrix_table):
    assert not check_if_correct(matrix_table)
