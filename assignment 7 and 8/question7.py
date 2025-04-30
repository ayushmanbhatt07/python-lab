# Create a class for representing any 2-D point or vector. The methods inside this class include
# its magnitude and its rotation with respect to the X-axis. Using the objects define functions for
# calculating the distance between two vectors, dot product, cross product of two vectors. Extend
# the 2-D vectors into 3-D using the concept of inheritance. Update the methods according to 3-
# D.
import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def angle_with_x_axis(self):
        return math.atan2(self.y, self.x)

    @staticmethod
    def distance(p1, p2):
        return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

    @staticmethod
    def dot_product(p1, p2):
        return p1.x * p2.x + p1.y * p2.y

    @staticmethod
    def cross_product(p1, p2):
        return p1.x * p2.y - p1.y * p2.x


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    @staticmethod
    def distance(p1, p2):
        return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2 + (p2.z - p1.z) ** 2)

    @staticmethod
    def dot_product(p1, p2):
        return p1.x * p2.x + p1.y * p2.y + p1.z * p2.z

    @staticmethod
    def cross_product(p1, p2):
        return Point3D(
            p1.y * p2.z - p1.z * p2.y,
            p1.z * p2.x - p1.x * p2.z,
            p1.x * p2.y - p1.y * p2.x
        )