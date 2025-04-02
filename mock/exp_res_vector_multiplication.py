from Vector import Vector
from mock.mock_vector import vectors, scalars, vector_scalar_pairs

# Expected values for (reverse) scalar multiplication

exp_vectors_mul = [
    Vector(x=vector.x * scalar, y=vector.y * scalar)
    for (vector, scalar) in vector_scalar_pairs
]


# Parametrization

expected_triplets_mul = list(zip(vectors, scalars, exp_vectors_mul))
