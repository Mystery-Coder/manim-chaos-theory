from manim import *
import random

class BarnsleyFern(Scene):
    def barnsley_point(self, x, y):
        """Apply one random transformation of the Barnsley Fern IFS."""
        r = random.random()
        if r < 0.01:
            return 0, 0.16 * y
        elif r < 0.86:
            return 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        elif r < 0.93:
            return 0.20 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        else:
            return -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44

    def construct(self):
        x, y = 0, 0
        dots = VGroup()

   
        n_points = 20000

        for _ in range(n_points):
            x, y = self.barnsley_point(x, y)
            # Scale and shift for display
            dot = Dot(point=[x / 2, y / 5 - 2, 0], radius=0.005, color=GREEN)
            dots.add(dot)

        self.add(*dots)
