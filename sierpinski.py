from manim import *
from random import randint

"""
Chaos Game:
Pick 3 points on the plane, A,B,C and a Starting point.
Roll a die, move from the start halfway to A, B or C based on
die roll -> A if 1,2
            B if 3,4
            C if 5,6
Over many iterations this forms a fractal known as the Sierpinksi Triangle
"""



class Sierpinski(Scene):

    def construct(self):
        axes = Axes()
        # self.add(axes)
        # Different quadrants to spread out the pattern
        A = [randint(1,4), randint(1,4)] # 1st quadrant
        B = [-randint(1,4), randint(1,4)] # 2nd quadrant
        C = [-randint(1,4), -randint(1,4)] # 3rd quadrant
        start = [randint(1,4), -randint(1,4)]      

        self.add(Dot(axes.c2p(A[0], A[1]), radius=0.08, color=RED))
        self.add(Dot(axes.c2p(B[0], B[1]), radius=0.08, color=RED))
        self.add(Dot(axes.c2p(C[0], C[1]), radius=0.08, color=RED))
        self.add(Dot(axes.c2p(start[0], start[1]), radius=0.08, color=WHITE))

        x = start

        ITERATIONS = 1200
        dots = []
        while ITERATIONS != 0:
            roll = randint(1,6)
            mid = []
            if roll in (1,2):
                # Calculate mid point between x and A
                mid = [(x[0] + A[0])/2, (x[1] + A[1])/2]
            elif roll in (3,4):
                mid = [(x[0] + B[0])/2, (x[1] + B[1])/2]
            else:
                mid = [(x[0] + C[0])/2, (x[1] + C[1])/2]

            # Calculate the dots, do chunk animation
            dots.append(Dot(axes.c2p(mid[0], mid[1]), radius=0.04, color=RED))
            x = mid
            ITERATIONS -= 1

        CHUNK = 300
        for i in range(0, len(dots), CHUNK):
            chunk = dots[i:i+CHUNK]
            self.play(*[FadeIn(dot, run_time=0.6) for dot in chunk])
        
            






        

        

