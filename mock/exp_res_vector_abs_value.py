import math

from mock.mock_vector import vectors

# Parametrization

expected_absolute_values = [math.sqrt(vector.x**2 + vector.y**2) for vector in vectors]

expected_pairs_abs = list(zip(vectors, expected_absolute_values))
