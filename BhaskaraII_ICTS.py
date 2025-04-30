from manim import *

class BhaskaraII_ICTS(Scene):
    def construct(self):

# color
        icts_grey="#9BAFC5"
        WHITE = "#fafafa"
        ICTS_MAROON = "#90403d"
        ICTS_HIGHLIGHT = "#F88826"
        ICTS_GREY = "#9BAFC5"
        self.camera.background_color = WHITE

# scale
        scale = 1/135

# length
        a_length = 245*scale
        b_length = 507*scale  

# points
        A = np.array([-(a_length+b_length)/2,-(b_length-a_length)/2,0])
        B = A + a_length*RIGHT
        C = B + b_length*UP
        mA = -A

        triangle = Polygon(A,B,C,stroke_color=WHITE,fill_color=ICTS_MAROON,fill_opacity=1,stroke_width=4)
        triangle2 = triangle.copy().rotate(PI/2).shift(DOWN*(a_length+b_length)/2+RIGHT*(b_length-a_length)/2)
        triangle3 = triangle2.copy().rotate(PI/2).shift(UP*(b_length-a_length)/2+RIGHT*(a_length+b_length)/2)
        triangle4 = triangle3.copy().rotate(PI/2).shift(UP*(a_length+b_length)/2+LEFT*(b_length-a_length)/2)
        self.play(FadeIn(triangle),FadeIn(triangle2),FadeIn(triangle3),FadeIn(triangle4))
        
        AC = C-A
        c_label = MathTex("$c$",color=BLACK).next_to(A,LEFT)
        perp = np.array([AC[1], -AC[0], 0])
        D = A + perp
        E = C + perp
        square = Polygon(A, C, E, D, stroke_color=BLACK)
        
        self.wait(2)
        self.play(Create(square),c_label,)
        self.wait(2)