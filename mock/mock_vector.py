from Vector import Vector

# Vectors for testing

vector_1 = Vector(1, 2)
vector_2 = Vector(1, 3)
vector_3 = Vector(-1, 2)
vector_4 = Vector(100, -100)
vector_5 = Vector(0, -43)

# Expected values for string representation

expected_string_1 = "Vector(1, 2)"
expected_string_2 = "Vector(1, 3)"
expected_string_3 = "Vector(-1, 2)"
expected_string_4 = "Vector(100, -100)"
expected_string_5 = "Vector(0, -43)"

# Parametrization for test

vectors = [
    vector_1,
    vector_2,
    vector_3,
    vector_4,
    vector_5,
]

exp_strings = [
    expected_string_1,
    expected_string_2,
    expected_string_3,
    expected_string_4,
    expected_string_5,
]

expected_pairs = list(zip(vectors, exp_strings))
