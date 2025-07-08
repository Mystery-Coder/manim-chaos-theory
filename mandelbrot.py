from manim import *


"""
The Mandelbrot Set is the set of all Complex Numbers, c
such that the function f(Z) = Z^2 + c, starting with Z = 0, stays bounded, it should not
diverge to infinity.
c = 1,

"""

class Mandelbrot(Scene):
    def construct(self):
        axes = Axes()

        self.add(axes)