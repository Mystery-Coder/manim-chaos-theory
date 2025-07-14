from manim import *


"""
The Mandelbrot Set is the set of all Complex Numbers, c
such that the sequence Zn+1 = Zn^2 + c, starting with a  Z0 = 0, stays bounded(it should not
diverge to infinity)

"""


def testMandelbrot(c, max_iterations=100):
    Z = 0
    for _ in range(max_iterations):
        Z = Z**2 + c

        if abs(Z) > 2:
            return False
    return True


class Mandelbrot(Scene):
    def construct(self):
        axes = Axes()

        self.add(axes)