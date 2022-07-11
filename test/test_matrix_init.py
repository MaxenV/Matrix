from random import randint
from random import choice
import pytest
from matrix_lib import Matrix


class TestMatrix__init__:
    @pytest.mark.parametrize(
        ("matrix_table"),
        (
            ([[4, 4.6, 3, 5], [7, -8, 5, 7], [2, 7, 3, 1], [6, -3, 4, 5]]),
            ([[4, -4.6, 3, 5]]),
            ([[-4, 4.6, 3, 5], [2, 7, 3, 1]]),
            ([[randint(-1000, 1000) for _ in range(45)],
             [randint(-1000, 1000) for _ in range(45)]]),
            ([[1, 0, 0, 0], [0, -10000, 0, 0], [0, 0, 1.09, 0], [0, 0, 0, 1]]),
            ([[0, 0, 0, 0], [0, 0, 0, 0], [0, -0, 0, 0], [0, 0, 0, 0]])
        )
    )
    def test_initializing_list_correct(self, matrix_table):
        result = Matrix(matrix_table)
        assert (
            result.matrix == matrix_table
            and result.rows == len(matrix_table)
            and result.columns == len(choice(matrix_table))
        )

    @pytest.mark.parametrize(
        ("matrix_table"),
        (
            "Some string",
            '"S"',
            4.6,
            True,
            {4, 5, 7, 2},
            {8: 5, "asd": 2, 4: "dd"},
            (([0, 0, 0, 0], [0, 0, 0, 0], [0, -0, 0, 0], [0, 0, 0, 0])),
            (((1), (4))),
            ((1, 4), (4, 7)),
        )
    )
    def test_initializing_list_type_err(self, matrix_table):
        with pytest.raises(TypeError):
            Matrix(matrix_table)

    def test_initializing_empty_arr(self):
        result = Matrix()
        assert (
            result.matrix == list() and
            result.columns == 0 and
            result.rows == 0
        )

    @pytest.mark.parametrize(
        ("matrix_table"),
        (
            (4, 5, 2),
            (([0, 0, 0, 0], [0, 0, 0, 0], [0, -0, 0, 0], [0, 0, 0, 0]),
             ([0, 0, 0, 0], [0, 0, 0, 0], [0, -0, 0, 0], [0, 0, 0, 0])),
            ([[4, 4.6, 3, 5], [7, -8, 5, 7], [2, 7, 3, 1], [6, -3, 4, 5]],
             [[4, -4.6, 3, 5]]),
            (4, 5.64, 5),
        )
    )
    def test_initializing_too_much_args(self, matrix_table):
        with pytest.raises(TypeError):
            Matrix(matrix_table)
