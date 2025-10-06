from manim import *
import random

class mathsCircle(Scene):
    def construct(self):
        icts_maroon = "#90403d"
        triangles = VGroup()
        for i in range(4):
            tri = Triangle(color=icts_maroon, fill_opacity=0.9)
            tri.set_height(1)
            tri.shift([
                random.uniform(-2*i, 2),
                random.uniform(-1, i),
                0
            ])
            triangles.add(tri)

        self.play(*[FadeIn(tri) for tri in triangles])
        self.wait(1)

