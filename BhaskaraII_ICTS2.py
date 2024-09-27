from manim import *

class BhaskaraII_ICTS(Scene):
    def construct(self):
        WHITE = "#fafafa"
        ICTS_MAROON = "#90403d"
        ICTS_HIGHLIGHT = "#F88826"
        ICTS_GREY = "#9BAFC5"

        a_length = 8 / 4
        b_length = 15 / 4

        A = np.array([-(a_length + b_length) / 2, -(b_length - a_length) / 2, 0])
        B = A + a_length * RIGHT
        C = B + b_length * UP
        mA = -A

        triangle = Polygon(A, B, C, stroke_color=WHITE, fill_color=ICTS_MAROON, fill_opacity=1, stroke_width=2)
        square_In = Polygon(B, B + UP * (b_length - a_length), B + UP * (b_length - a_length) + RIGHT * (b_length - a_length),
                            B + RIGHT * (b_length - a_length), fill_opacity=0.2, color=ICTS_GREY, stroke_width=0)

        lines = [
            Line(A, C, color=BLACK),
            Line(A, A + RIGHT * b_length, color=ICTS_HIGHLIGHT),
            Line(C, C + DOWN * b_length, color=ICTS_HIGHLIGHT),
            Line(mA, mA + LEFT * b_length, color=ICTS_HIGHLIGHT),
            Line(-C, -C + UP * b_length, color=ICTS_HIGHLIGHT),
            Line(A, A + RIGHT * a_length, color=ICTS_GREY),
            Line(C, C + DOWN * a_length, color=ICTS_GREY),
            Line(-A, -A + LEFT * a_length, color=ICTS_GREY),
            Line(-C, -C + UP * a_length, color=ICTS_GREY),
        ]

        labels = [
            Tex("$c$", color=BLACK).next_to(lines[0].get_center(), LEFT),
            Tex("$a$", color=ICTS_HIGHLIGHT).next_to(lines[1].get_center(), DOWN),
            Tex("$a$", color=ICTS_HIGHLIGHT).next_to(lines[2].get_center(), LEFT),
            Tex("$a$", color=ICTS_HIGHLIGHT).next_to(lines[3].get_center(), UP),
            Tex("$a$", color=ICTS_HIGHLIGHT).next_to(lines[4].get_center(), RIGHT),
            Tex("$b$", color=ICTS_GREY).next_to(lines[5].get_center(), UP),
            Tex("$b$", color=ICTS_GREY).next_to(lines[6].get_center(), RIGHT),
            Tex("$b$", color=ICTS_GREY).next_to(lines[7].get_center(), DOWN),
            Tex("$b$", color=ICTS_GREY).next_to(lines[8].get_center(), LEFT),
        ]

        triangles = [triangle.copy().rotate(PI / 2).shift(DOWN * (a_length + b_length) / 2 + RIGHT * (b_length - a_length) / 2),
                     triangle.copy().rotate(PI / 2).shift(UP * (b_length - a_length) / 2 + RIGHT * (a_length + b_length) / 2),
                     triangle.copy().rotate(PI / 2).shift(UP * (a_length + b_length) / 2 + LEFT * (b_length - a_length) / 2),
                     triangle.copy().rotate(PI).shift(RIGHT * b_length + UP * a_length)]

        right_angles = [
            RightAngle(lines[0], lines[1], stroke_width=4),
            RightAngle(lines[2], lines[1], stroke_width=4, quadrant=(-1, -1)),
            RightAngle(lines[3], lines[2], stroke_width=4),
            RightAngle(lines[0], lines[3], stroke_width=4, quadrant=(-1, -1)),
            RightAngle(lines[5], lines[2], stroke_width=3, quadrant=(-1, -1)),
            RightAngle(lines[8], lines[1], stroke_width=3, quadrant=(-1, -1)),
            RightAngle(lines[7], lines[4], stroke_width=3, quadrant=(-1, -1)),
            RightAngle(lines[6], lines[3], stroke_width=3, quadrant=(-1, -1)),
        ]

        angles = [
            Angle(lines[5], lines[0], radius=0.4, color=ICTS_GREY),
            Angle(lines[0], lines[1], radius=0.4, color=ICTS_HIGHLIGHT),
            Angle(lines[2], lines[4], radius=0.4, color=ICTS_GREY),
            Angle(lines[3], lines[6], radius=0.4, color=ICTS_HIGHLIGHT),
            Angle(lines[7], lines[5], radius=0.4, color=ICTS_GREY),
            Angle(lines[6], lines[2], radius=0.4, color=ICTS_HIGHLIGHT),
            Angle(lines[1], lines[8], radius=0.4, color=ICTS_GREY),
            Angle(lines[4], lines[7], radius=0.4, color=ICTS_HIGHLIGHT),
        ]

        angle_labels = [
            MathTex(r"90^{\circ}-\theta", font_size=28, color=ICTS_GREY).next_to(angles[0], UR, buff=0),
            MathTex(r"\theta", font_size=28, color=ICTS_HIGHLIGHT).next_to(angles[1], DOWN, buff=0.1),
        ]

        pythagorean_theorem = [
            Tex("$c^2$", color=BLACK).shift(DOWN * 2.9 + LEFT),
            Tex("$=$", color=BLACK).next_to(pythagorean_theorem[0]),
            Tex("$a^2$", color=BLACK).next_to(pythagorean_theorem[1]),
            Tex("$+$", color=BLACK).next_to(pythagorean_theorem[2]),
            Tex("$b^2$", color=BLACK).next_to(pythagorean_theorem[3]),
        ]

        icts_tifr = Tex("ICTS - TIFR", color=BLACK).shift(DOWN * 2.9)
        square_a = Polygon(A, A + RIGHT * b_length, A + RIGHT * b_length + UP * b_length, A + UP * b_length,
                           color=ICTS_HIGHLIGHT, stroke_width=0, fill_opacity=0.5).shift(DOWN * a_length / 2 + RIGHT * a_length)
        square_b