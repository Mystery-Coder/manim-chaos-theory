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
        SCALE = 3.6
        # Start from a random point
        X = np.array([randint(-1, 1), randint(-1, 1)], dtype=float)

        dots = []
        for _ in range(ITERATIONS):

            f1 = A @ X
            f2 = (B @ X) - C
            
            # X = f1 if randint(0, 1) else f2
            dot = Dot(SCALE*axes.c2p(X[0], X[1]), radius=0.02)

            if randint(0,1) == 1:
                dot.set_color(BLUE)
                X = f1
            else:
                dot.set_color(BLUE)
                X = f2

            dots.append(dot)


        # Animate dots together
        CHUNK_SIZE = 500
        for i in range(0, len(dots), CHUNK_SIZE):
            chunk = dots[i:i+CHUNK_SIZE]
            self.play(*[FadeIn(dot, run_time=0.3) for dot in chunk])



        self.wait(2)
