import math


class Vector:
    """
    Glossary of available methods:

    __repr__ - print debug statements
    __abs__ - return the absolute value of a vector
    __eq__ - checks if two vectors are equal
    __add__ - addition of a vector with another vector
    __radd__ - addition of a vector with another vector
    __sub__ - subtraction of a vector with another vector
    __rsub__ - subtraction of a vector with another vector
    __mul__ - multiplication of a vector with a scalar
    __rmul__ - multiplication of a scalar with a vector
    __truediv__ - division of a vector by a scalar
    cdot - scalar product between two vectors
    normalize - normalizes vector to a modulus of unity
    check_scalar - checks if an object is a float or an int
    check_vector - checks if an object an instance of Vector
    """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, vector):
        self._check_vector(vector_candidate=vector)
        return math.isclose(self.x, vector.x) and math.isclose(self.y, vector.y)

    def __add__(self, vector: "Vector") -> "Vector":
        self._check_vector(vector_candidate=vector)
        x = self.x + vector.x
        y = self.y + vector.y
        return Vector(x, y)

    def __radd__(self, vector: "Vector") -> "Vector":
        self._check_vector(vector_candidate=vector)
        x = self.x + vector.x
        y = self.y + vector.y
        return Vector(x, y)

    def __sub__(self, vector: "Vector") -> "Vector":
        self._check_vector(vector_candidate=vector)
        x = self.x - vector.x
        y = self.y - vector.y
        return Vector(x, y)

    def __rsub__(self, vector: "Vector") -> "Vector":
        self._check_vector(vector_candidate=vector)
        x = vector.x - self.x
        y = vector.y - self.y
        return Vector(x, y)

    def __mul__(self, scalar: float) -> "Vector":
        self._check_scalar(scalar_candidate=scalar)
        x = scalar * self.x
        y = scalar * self.y
        return Vector(x, y)

    def __rmul__(self, scalar: float) -> "Vector":
        self._check_scalar(scalar_candidate=scalar)
        x = scalar * self.x
        y = scalar * self.y
        return Vector(x, y)

    def __truediv__(self, scalar: float) -> "Vector":
        self._check_scalar(scalar_candidate=scalar)
        x = self.x / scalar
        y = self.y / scalar
        return Vector(x, y)

    def cdot(self, vector: "Vector") -> float:
        self._check_vector(vector_candidate=vector)
        x = self.x * vector.x
        y = self.y * vector.y
        return x + y

    def normalize(self) -> "Vector":
        return self / abs(self)

    @staticmethod
    def _check_scalar(scalar_candidate):
        if not (isinstance(scalar_candidate, float) or isinstance(scalar_candidate, int)):
            raise TypeError(
                f"The object ({scalar_candidate}, {type(scalar_candidate)} must be a Scalar."
            )

    @staticmethod
    def _check_vector(vector_candidate):
        if not isinstance(vector_candidate, Vector):
            raise TypeError(
                f"The object ({vector_candidate}, {type(vector_candidate)}) must be a Vector."
            )
