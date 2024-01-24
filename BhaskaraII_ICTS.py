from manim import *

class BhaskaraII_ICTS(Scene):
    def construct(self):
        white="#fafafa"
        self.camera.background_color = white
        icts_maroon = "#90403d"
        a_length = 8/4
        b_length = 15/4  

        A = [-(a_length+b_length)/2,-(b_length-a_length)/2,0]
        B = A + a_length*RIGHT
        C = B + b_length*UP

        triangle = Polygon(A,B,C,stroke_color=white,fill_color=icts_maroon,fill_opacity=1,stroke_width=2)
        triangle2 = triangle.copy().rotate(PI/2).shift(DOWN*(a_length+b_length)/2+RIGHT*(b_length-a_length)/2)
        triangle3 = triangle2.copy().rotate(PI/2).shift(UP*(b_length-a_length)/2+RIGHT*(a_length+b_length)/2)
        triangle4 = triangle3.copy().rotate(PI/2).shift(UP*(a_length+b_length)/2+LEFT*(b_length-a_length)/2)

        line1 = Line(A,C,color=BLACK)
        line2 = line1.copy().rotate(-PI/2,about_point=A)
        line3 = line2.copy().rotate(-PI/2,about_point=line2.get_end())
        line4 = line1.copy().rotate(PI/2,about_point=C)
        c_label = Tex("$c$",color=BLACK).next_to(line1.get_center(),LEFT)
        c_label2 = Tex("$c$",color=BLACK).next_to(line2.get_center(),DOWN)
        c_label3 = Tex("$c$",color=BLACK).next_to(line3.get_center(),RIGHT)
        c_label4 = Tex("$c$",color=BLACK).next_to(line4.get_center(),UP)

        rightangles1 = RightAngle(line1, line2,stroke_width=4)
        rightangles2 = RightAngle(line3, line2,stroke_width=4,quadrant=(-1,-1))
        rightangles3 = RightAngle(line4, line3,stroke_width=4)
        rightangles4 = RightAngle(line1, line4,stroke_width=4,quadrant=(-1,-1))

        linea1 = Line(A,A+RIGHT*b_length,color=BLUE)
        # self.play(FadeIn(triangle),FadeIn(triangle2),FadeIn(triangle3),FadeIn(triangle4))
        self.add(triangle,triangle2,triangle3,triangle4,rightangles1,rightangles2,rightangles4,rightangles3,line1,line2,line3,line4,c_label,c_label2,c_label3,c_label4,linea1,linea2)
        self.wait(2)


        # A = ORIGIN
        # B = A + square_side_length * np.array([np.cos(tilt_angle), np.sin(tilt_angle), 0])
        # C = B + square_side_length * np.array([np.cos(tilt_angle), np.sin(tilt_angle),0])

        # triangle = Polygon(A,B,C)
        # self.play(Create(triangle))