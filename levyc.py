from manim import *
import numpy as np
from random import randint
"""
Levy C Curve,
    
A = [
    0.5 0.5
    -0.5 0.5
]
B = transpose(A)

C = [
    0.5
    0.5
]

f1(x) = Ax
f2(x) = Bx - C


Apply both f1 and f2 to a random x, select either f1 or f2 output point
and apply the transformations again repeating for 25k times

"""
class LevyC(Scene):
    def construct(self):

        axes = Axes()
 

        A = np.array([[0.5, 0.5],
                      [-0.5, 0.5]])
        B = A.T
        C = np.array([0.5, 0.5])

        ITERATIONS = 2500
        SCALE = 4
        # Start from a random point
        X = np.array([randint(-1, 1), randint(-1, 1)], dtype=float)
        points = []

        for _ in range(ITERATIONS):
            points.append(SCALE*axes.c2p(X[0], X[1]))


            f1 = A @ X
            f2 = (B @ X) - C

            X = f1 if randint(0, 1) else f2


        # Animate dots together
        CHUNK_SIZE = 500
        for i in range(0, len(points), CHUNK_SIZE):
            chunk = points[i:i+CHUNK_SIZE]
            dots = [Dot(p, radius=0.02, color=(RED if (i+j)%4 < 2 else BLUE)) for j,p in enumerate(chunk)]
            self.play(*[FadeIn(dot, run_time=0.3) for dot in dots])

        self.wait(2)
