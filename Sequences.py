from manim import *

class ShowWrite(Scene):
    def construct(self):
        self.play(Write(Text("12, 11", font_size=144)))