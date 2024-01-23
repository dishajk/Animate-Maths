from manim import *

class BhaskaraII_ICTS(Scene):
    def construct(self):
        square_side_length = 4
        tilt_angle = PI / 3

        # A = ORIGIN
        # B = A + square_side_length * np.array([np.cos(tilt_angle), np.sin(tilt_angle), 0])
        # C = B + square_side_length * np.array([np.cos(tilt_angle), np.sin(tilt_angle),0])

        # triangle = Polygon(A,B,C)
        # self.play(Create(triangle))

        square3 = Square(side_length=square_side_length, color=GREEN).rotate(tilt_angle)
        self.play(FadeIn(square3))

        labels = VGroup(
            Tex("c").move_to(square3.get_corner(UL)+DOWN*1.6+RIGHT*0.7),
            Tex("c").move_to(square3.get_corner(DL)+UP*0.7+RIGHT*1.6),
            Tex("c").move_to(square3.get_corner(DR)+UP*1.6+LEFT*0.7),
            Tex("c").move_to(square3.get_corner(UR)+DOWN*0.7+LEFT*1.6),
        )

        self.play(FadeIn(labels))
        self.wait(2)