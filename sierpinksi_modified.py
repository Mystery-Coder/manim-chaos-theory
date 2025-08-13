from manim import *
from random import randint

"""
Modification of sierpinski.py to use section formula.
The point is moved to a point which divides the line in the ratio, m:n.
The Sierpinski Triangle is generated when m:n = 1:1
"""



class SierpinskiModified(Scene):

    def construct(self):
        axes = Axes()
        # self.add(axes)
        # Different quadrants to spread out the pattern
        A = [randint(1,4), randint(1,4)] # 1st quadrant
        B = [-randint(1,4), randint(1,4)] # 2nd quadrant
        C = [-randint(1,4), -randint(1,4)] # 3rd quadrant
        start = [randint(1,4), -randint(1,4)]

        m = 1
        n = 1.618

        self.add(Dot(axes.c2p(A[0], A[1]), radius=0.1, color=RED))
        self.add(Dot(axes.c2p(B[0], B[1]), radius=0.1, color=RED))
        self.add(Dot(axes.c2p(C[0], C[1]), radius=0.1, color=RED))
        self.add(Dot(axes.c2p(start[0], start[1]), radius=0.1, color=WHITE))

        x = start

        ITERATIONS = 2500
        # dots = []
        while ITERATIONS != 0:
            roll = randint(1,6)
            point = []
            # Calculate section formula
            if roll in (1,2):
                point = [(m*A[0] + n*x[0])/(m + n), (m*A[1] + n*x[1])/(m+n)]
            elif roll in (3,4):
                point = [(m*B[0] + n*x[0])/(m + n), (m*B[1] + n*x[1])/(m+n)]
            else:
                point = [(m*C[0] + n*x[0])/(m + n), (m*C[1] + n*x[1])/(m+n)]

            x = point
            self.add(Dot(axes.c2p(point[0], point[1]), radius=0.04, color=RED))

            # Calculate the dots, do chunk animation
            # dots.append(Dot(axes.c2p(mid[0], mid[1]), radius=0.04, color=RED))
            # x = mid
            ITERATIONS -= 1

        # CHUNK = 500
        # for i in range(0, len(dots), CHUNK):
        #     self.play(*[FadeIn(dot, run_time=0.5) for dot in dots])
        
            






        

        

