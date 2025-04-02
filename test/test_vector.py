import pytest

from mock.exp_res_vector_true_division import expected_triplets_true_div
from mock.mock_vector import vectors
from mock.exp_res_vector_string import expected_pairs_str
from mock.exp_res_vector_abs_value import expected_pairs_abs
from mock.exp_res_vector_multiplication import expected_triplets_mul
from mock.exp_res_vector_addition import expected_triplets_add, expected_triplets_radd
from mock.exp_res_vector_subtraction import (
    expected_triplets_sub,
    expected_triplets_rsub,
)


@pytest.mark.parametrize("vector, expected_value", expected_pairs_str)
def test_vector_string_generation(vector, expected_value):
    assert str(vector) == expected_value


@pytest.mark.parametrize("vector, expected_value", expected_pairs_abs)
def test_vector_absolute_value(vector, expected_value):
    assert abs(vector) == expected_value


@pytest.mark.parametrize(
    "vector_1, vector_2, expected_value", [(vector, vector, True) for vector in vectors]
)
def test_vector_equality(vector_1, vector_2, expected_value):
    assert (vector_1 == vector_2) is True


@pytest.mark.parametrize("vector_1, vector_2, expected_value", expected_triplets_add)
def test_vector_addition(vector_1, vector_2, expected_value):
    assert (vector_1 + vector_2) == expected_value


@pytest.mark.parametrize("vector_1, vector_2, expected_value", expected_triplets_radd)
def test_vector_r_addition(vector_1, vector_2, expected_value):
    assert (vector_1 + vector_2) == expected_value


@pytest.mark.parametrize("vector_1, vector_2, expected_value", expected_triplets_sub)
def test_vector_subtraction(vector_1, vector_2, expected_value):
    assert (vector_1 - vector_2) == expected_value


@pytest.mark.parametrize("vector_1, vector_2, expected_value", expected_triplets_rsub)
def test_vector_r_subtraction(vector_1, vector_2, expected_value):
    assert (vector_2 - vector_1) == expected_value


@pytest.mark.parametrize("vector, scalar, expected_value", expected_triplets_mul)
def test_vector_multiplication(vector, scalar, expected_value):
    assert vector * scalar == expected_value


@pytest.mark.parametrize("vector, scalar, expected_value", expected_triplets_mul)
def test_vector_r_multiplication(vector, scalar, expected_value):
    assert scalar * vector == expected_value


@pytest.mark.parametrize("vector, scalar, expected_value", expected_triplets_true_div)
def test_vector_true_division(vector, scalar, expected_value):
    assert vector / scalar == expected_value


@pytest.mark.parametrize("vector", vectors)
def test_vector_true_division_by_zero(vector):
    with pytest.raises(ZeroDivisionError):
        _ = vector / 0


# TODO: Unit Test for cdot
# TODO: Unit Test for normalize
