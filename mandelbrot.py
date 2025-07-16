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
        
        axes = Axes(
            x_range=[-2.5, 1.5, 0.5],
            y_range=[-2, 2, 0.5],
            x_length=10,
            y_length=8

        ).add_coordinates()

        dots = []

        # Step size controls resolution
        step = 0.01
        for x in frange(-2.0, 1.0, step):
            for y in frange(-1.5, 1.5, step):
                c = complex(x, y)
                if testMandelbrot(c, max_iterations=50):
                    dot = Dot(axes.c2p(x, y), radius=0.01, color=WHITE)
                    dots.append(dot)

        self.add(*dots)

def frange(start, stop, step):
    while start < stop:
        yield start
        start += step
