import itertools


class Polygon(object):
    """A polygon class
    """

    def __init__(self, *sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

    def is_valid(self):
        raise NotImplementedError

    def is_regular(self):
        side = self.sides[0]
        return all([x == side for x in self.sides[1:]])

    def area(self):
        raise NotImplementedError


class InvaliPolygonError(Exception):
    pass



class Triangle(object):

    def __init__(self, *sides):
        self.polygon = Polygon(*sides)

    def perimeter(self):
        return self.polygon.perimeter()

    def is_valid(self, f):
        def inner(self, *args):
            perimeter = self.polygon.perimeter()
            sides = self.polygon.sides()

            for side in sides:
                sum_two = perimeter - side
                if sum_two <= side:
                    raise InvaliPolygonError(str(self.__class__) + "is invalid!")
            result = f(self, *args)
            return result
        return inner()

    @is_valid()
    def is_equilateral(self):
        return self.polygon.is_regular()

    @is_valid()
    def is_isosceles(self):
        return any(a == b for a, b in itertools.combinations(self.sides, 2))

    @is_valid()
    def area(self):
        p = self.polygon.perimeter() / 2.0
        total = p
        for side in self.polygon.sides:
            total *= abs(p-side)
        return pow(total, 0.5)

class Rectangle(object):

    method_mapper = {'is_square': 'is_regular'}

    def __init__(self, *sides):
        self.polygon = Polygon(*sides)
