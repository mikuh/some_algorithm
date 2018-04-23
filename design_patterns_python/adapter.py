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


class Triangle(Polygon):

    def is_equilateral(self):
        if self.is_valid():
            return super(Triangle, self).is_regular()

    def is_isosceles(self):

        if self.is_valid():
            return any(a == b for a, b in itertools.combinations(self.sides, 2))
        return False

    def area(self):
        p = self.perimeter() / 2.0
        total = p
        for side in self.sides:
            total *= abs(p-side)
        return pow(total, 0.5)

    def is_valid(self):
        perimeter = self.perimeter()
        for side in self.sides:
            sum_two = perimeter - side
            if sum_two <= side:
                raise InvaliPolygonError(str(self.__class__) + "is invalid!")
        return True


class Rectangle(Polygon):

    def is_square(self):
        if self.is_valid():
            return self.is_regular()

    def is_valid(self):
        if len(self.sides) != 4:
            return False

        for a, b in [(0, 2), (1, 3)]:
            if self.sides[a] != self.sides[b]:
                return False
        return True

    def area(self):
        if self.is_valid():
            return self.sides[0] * self.sides[1]



t1 = Triangle(20, 20, 20)
print(t1.is_valid())
print(t1.is_equilateral())
print(t1.is_isosceles())
print(t1.area())

t2 = Triangle(10, 20, 30)
t2.is_valid()