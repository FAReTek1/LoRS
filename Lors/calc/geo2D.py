"""
Basic 2D geometrical functions and classes for use elsewhere in the library
"""
import math

print("Imported geo2D")


class Node2D:
    """
    A 2-dimensional node with an x & y
    """

    def __init__(self, x: float, y: float, data=None):
        self.x = x
        self.y = y
        self.data = data

    def __repr__(self):
        return f"Node2D({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __iter__(self):
        yield self.x
        yield self.y

    def __add__(self, other):
        return Node2D(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return Node2D(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Node2D(
                other * self.x,
                other * self.y
            )
        else:
            raise TypeError(
                "Can only multiply Node2D with numbers - float or int"
            )

    def __truediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Node2D(
                other * self.x,
                other * self.y
            )
        else:
            raise TypeError(
                "Can only divide Node2D with numbers - float or int"
            )

    def __neg__(self):
        return Node2D(
            -self.x,
            -self.y
        )

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __complex__(self):
        return self.x + self.y * 1j

    def __round__(self, n=None):
        return Node2D(
            round(self.x, n),
            round(self.y, n)
        )

    def __trunc__(self):
        return Node2D(
            math.trunc(self.x),
            math.trunc(self.y)
        )

    def __floor__(self):
        return Node2D(
            math.floor(self.x),
            math.floor(self.y)
        )

    def __ceil__(self):
        return Node2D(
            math.ceil(self.x),
            math.ceil(self.y)
        )

