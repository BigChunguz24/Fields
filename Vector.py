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
    __cdot__ - scalar product between two vectors
    normalize - normalizes vector to a modulus of unity
    check_scalar - checks if an object is a floar or an int
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
        self.check_vector(vector=vector)
        return math.isclose(self.x, vector.x) and math.isclose(self.y, vector.y)

    def __add__(self, vector: "Vector") -> "Vector":
        self.check_vector(vector=vector)
        x = self.x + vector.x
        y = self.y + vector.y
        return Vector(x, y)

    def __radd__(self, vector: "Vector") -> "Vector":
        self.check_vector(vector=vector)
        x = self.x + vector.x
        y = self.y + vector.y
        return Vector(x, y)

    def __sub__(self, vector: "Vector") -> "Vector":
        self.check_vector(vector=vector)
        x = self.x - vector.x
        y = self.y - vector.y
        return Vector(x, y)

    def __rsub__(self, vector: "Vector") -> "Vector":
        self.check_vector(vector=vector)
        x = vector.x - self.x
        y = vector.y - self.y
        return Vector(x, y)

    def __mul__(self, scalar: float) -> "Vector":
        self.check_scalar(scalar=scalar)
        x = scalar * self.x
        y = scalar * self.y
        return Vector(x, y)

    def __rmul__(self, scalar: float) -> "Vector":
        self.check_scalar(scalar=scalar)
        x = scalar * self.x
        y = scalar * self.y
        return Vector(x, y)

    def __truediv__(self, scalar: float) -> "Vector":
        self.check_scalar(scalar=scalar)
        x = self.x / scalar
        y = self.y / scalar
        return Vector(x, y)

    def cdot(self, vector: "Vector") -> float:
        self.check_vector(vector=vector)
        x = self.x * vector.x
        y = self.y * vector.y
        return x + y

    def normalize(self) -> "Vector":
        vector = Vector(x=self.x, y=self.y)
        return vector / abs(vector)

    @staticmethod
    def check_scalar(scalar):
        if not (isinstance(scalar, float) or isinstance(scalar, int)):
            raise TypeError(
                f"The added object ({scalar}, {type(scalar)} must be a Scalar."
            )

    @staticmethod
    def check_vector(vector):
        if not isinstance(vector, Vector):
            raise TypeError(
                f"The added object ({vector}, {type(vector)}) must be a Vector."
            )


if __name__ == "__main__":
    x = Vector(x=0.1, y=0.1)
    y = Vector(x=0.2, y=0.2)
    z = Vector(x=0.3, y=0.3)

    print (x+y == z)