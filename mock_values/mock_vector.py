from Vector import Vector


# Vectors for testing

vector_1 = Vector(1, 2)
vector_2 = Vector(1, 3)
vector_3 = Vector(-1, 2)
vector_4 = Vector(100, -100)
vector_5 = Vector(0, -43)

vectors = [
    vector_1,
    vector_2,
    vector_3,
    vector_4,
    vector_5,
]


# Additional vectors for addition/r_addition testing

vector_1a = Vector(2, 1)
vector_2a = Vector(6, -3)
vector_3a = Vector(-4, -5)
vector_4a = Vector(9, 0)
vector_5a = Vector(7, -57)

vectors_a = [vector_1a, vector_2a, vector_3a, vector_4a, vector_5a]


# Scalars to multiply/divide by

scalar_1 = 2
scalar_2 = 5
scalar_3 = 70
scalar_4 = 12
scalar_5 = -8

scalars = [
    scalar_1,
    scalar_2,
    scalar_3,
    scalar_4,
    scalar_5,
]

vector_scalar_pairs = list(zip(vectors, scalars))
