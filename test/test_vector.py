import pytest

from Vector import Vector

a = Vector(3, 5)
b = Vector(2, 4)


@pytest.mark.parametrize(
    "vector, expected", [(a, "Vector(3, 5)"), (b, "Vector(2, " "4)")]
)
def test_vector_string_generation(vector, expected):
    assert str(vector) == expected
