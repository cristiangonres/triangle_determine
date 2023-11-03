"""Determine if a triangle is equilateral, isosceles, or scalene."""

def test_triangle(sides):
    """test triangles isosceles and scalene"""
    sidea, sideb, sidec = sorted(sides)
    return all(sides) and sidea + sideb > sidec


def equilateral(sides):
    """An equilateral triangle has all three sides the same length."""
    sidea, sideb, sidec = sides
    return sidea == sideb == sidec and test_triangle(sides)


def isosceles(sides):
    """An isosceles triangle has at least two sides the same length."""
    return test_triangle(sides) and len(set(sides)) <= 2


def scalene(sides):
    """A scalene triangle has all sides of different lengths."""
    return test_triangle(sides) and len(set(sides)) == 3
