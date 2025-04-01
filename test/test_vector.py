import pytest

from mock.mock_vector import expected_pairs


@pytest.mark.parametrize("vector, expected_value", expected_pairs)
def test_vector_string_generation(vector, expected_value):
    assert str(vector) == expected_value
