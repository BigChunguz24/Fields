import pytest

from Vector import Vector
from mock.mock_vector import expected_pairs

a = Vector(3, 5)
b = Vector(2, 4)


@pytest.mark.parametrize("vector, expected_value", expected_pairs)
def test_vector_string_generation(vector, expected_value):
    assert str(vector) == expected_value
