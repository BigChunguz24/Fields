from Vector import Vector

from mock_values.mock_vector import vectors, vectors_a


# Expected values for vector addition

exp_vector_1 = Vector(3, 3)
exp_vector_2 = Vector(7, 0)
exp_vector_3 = Vector(-5, -3)
exp_vector_4 = Vector(109, -100)
exp_vector_5 = Vector(7, -100)


# Parametrization (both for __add__ and __radd__)

exp_vectors_addition = [
    exp_vector_1,
    exp_vector_2,
    exp_vector_3,
    exp_vector_4,
    exp_vector_5,
]

expected_triplets_add = list(zip(vectors, vectors_a, exp_vectors_addition))
expected_triplets_radd = list(zip(vectors_a, vectors, exp_vectors_addition))
