from Vector import Vector

from mock_values.mock_vector import vectors, vectors_a

# Expected values for vector (reverse) subtraction

exp_vector_1_sub = Vector(-1, 1)
exp_vector_2_sub = Vector(-5, 6)
exp_vector_3_sub = Vector(3, 7)
exp_vector_4_sub = Vector(91, -100)
exp_vector_5_sub = Vector(-7, 14)

exp_vector_1_rsub = Vector(1, -1)
exp_vector_2_rsub = Vector(5, -6)
exp_vector_3_rsub = Vector(-3, -7)
exp_vector_4_rsub = Vector(-91, 100)
exp_vector_5_rsub = Vector(7, -14)


# Parametrization (both for __sub__ and __rsub__)

exp_vectors_subtraction = [
    exp_vector_1_sub,
    exp_vector_2_sub,
    exp_vector_3_sub,
    exp_vector_4_sub,
    exp_vector_5_sub,
]

exp_vectors_r_subtraction = [
    exp_vector_1_rsub,
    exp_vector_2_rsub,
    exp_vector_3_rsub,
    exp_vector_4_rsub,
    exp_vector_5_rsub,
]

expected_triplets_sub = list(zip(vectors, vectors_a, exp_vectors_subtraction))
expected_triplets_rsub = list(zip(vectors, vectors_a, exp_vectors_r_subtraction))
