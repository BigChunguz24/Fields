from mock.mock_vector import vectors


# Expected values for string representation

expected_string_1 = "Vector(1, 2)"
expected_string_2 = "Vector(1, 3)"
expected_string_3 = "Vector(-1, 2)"
expected_string_4 = "Vector(100, -100)"
expected_string_5 = "Vector(0, -43)"


# Parametrization

exp_strings = [
    expected_string_1,
    expected_string_2,
    expected_string_3,
    expected_string_4,
    expected_string_5,
]

expected_pairs_str = list(zip(vectors, exp_strings))
